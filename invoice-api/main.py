from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import date

from models import Invoice
from schemas import InvoiceIn, InvoiceOut
import store
from report import build_report

app = FastAPI(title="Invoice API", version="1.0.0")

# Configure CORS for your frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_FILE = "invoices.json"

@app.get("/api/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/invoices", response_model=List[InvoiceOut])
def list_invoices():
    invoices = store.load_invoices(DB_FILE)
    return [
        InvoiceOut(
            id=idx + 1,
            client=inv.client,
            amount=inv.amount,
            due_date=inv.due_date,
            paid=inv.paid
        )
        for idx, inv in enumerate(invoices)
    ]

@app.get("/api/invoices/report")
def get_invoice_report():
    invoices = store.load_invoices(DB_FILE)
    return build_report(invoices)

@app.get("/api/invoices/{id}", response_model=InvoiceOut)
def get_invoice(id: int):
    invoices = store.load_invoices(DB_FILE)
    if id < 1 or id > len(invoices):
        raise HTTPException(status_code=404, detail="Invoice not found")
    inv = invoices[id - 1]
    return InvoiceOut(
        id=id,
        client=inv.client,
        amount=inv.amount,
        due_date=inv.due_date,
        paid=inv.paid
    )

@app.post("/api/invoices", response_model=InvoiceOut, status_code=status.HTTP_201_CREATED)
def create_invoice(invoice_in: InvoiceIn):
    try:
        new_invoice = Invoice(
            client=invoice_in.client,
            amount=invoice_in.amount,
            due_date=invoice_in.due_date,
            paid=invoice_in.paid  # <-- Change this from getattr to invoice_in.paid
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    
    invoices = store.load_invoices(DB_FILE)
    invoices.append(new_invoice)
    store.save_invoices(DB_FILE, invoices)
    
    new_id = len(invoices)
    return InvoiceOut(
        id=new_id,
        client=new_invoice.client,
        amount=new_invoice.amount,
        due_date=new_invoice.due_date,
        paid=new_invoice.paid
    )