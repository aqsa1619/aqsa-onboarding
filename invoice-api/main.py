from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import Base, engine, get_db
from db_models import InvoiceRow
from models import Invoice
from report import build_report
from schemas import InvoiceIn, InvoiceOut

Base.metadata.create_all(engine)  # creates invoice.db and the table if missing

app = FastAPI(title="Invoice API", version="1.0.0")

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


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/invoices", response_model=List[InvoiceOut])
def list_invoices(db: Session = Depends(get_db)):
    return db.query(InvoiceRow).order_by(InvoiceRow.id).all()


@app.get("/api/invoices/report")
def get_invoice_report(db: Session = Depends(get_db)):
    rows = db.query(InvoiceRow).all()
    return build_report(rows)


@app.get("/api/invoices/{id}", response_model=InvoiceOut)
def get_invoice(id: int, db: Session = Depends(get_db)):
    row = db.get(InvoiceRow, id)
    if row is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return row


@app.post("/api/invoices", response_model=InvoiceOut, status_code=status.HTTP_201_CREATED)
def create_invoice(invoice_in: InvoiceIn, db: Session = Depends(get_db)):
    try:
        # reuse your existing validation in models.py
        checked = Invoice(
            client=invoice_in.client,
            amount=invoice_in.amount,
            due_date=invoice_in.due_date,
            paid=invoice_in.paid,
        )
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

    row = InvoiceRow(
        client=checked.client,
        amount=checked.amount,
        due_date=checked.due_date,
        paid=checked.paid,
    )
    db.add(row)        # put it in the basket
    db.commit()        # save it
    db.refresh(row)    # load the new id
    return row