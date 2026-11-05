"""PLACEHOLDER: replace with your real report.py logic."""
from models import Invoice


def build_report(invoices: list[Invoice]) -> dict:
    total = sum(i.amount for i in invoices)
    paid = sum(i.amount for i in invoices if i.paid)
    return {
        "count": len(invoices),
        "total": round(total, 2),
        "paid_total": round(paid, 2),
        "unpaid_total": round(total - paid, 2),
    }