import store
from db import Base, engine, SessionLocal
from db_models import InvoiceRow

Base.metadata.create_all(engine)
db = SessionLocal()

if db.query(InvoiceRow).count() > 0:
    print("Database already has invoices, skipping import.")
else:
    invoices = store.load_invoices("invoices.json")
    for inv in invoices:
        db.add(InvoiceRow(client=inv.client, amount=inv.amount,
                          due_date=inv.due_date, paid=inv.paid))
    db.commit()
    print(f"Imported {len(invoices)} invoices")

db.close()