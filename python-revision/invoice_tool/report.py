
from models import Invoice
from datetime import date


def total_by_client(invoices: list[Invoice]) -> dict[str, float]:

    totals = {}

    for invoice in invoices:

        if invoice.client not in totals:
            totals[invoice.client] = 0.0

        totals[invoice.client] += invoice.amount

    return totals


def overdue(invoices: list[Invoice], today: date) -> list[Invoice]:

    overdue_invoices = []

    for invoice in invoices:

        if not invoice.paid and invoice.due_date < today:
            overdue_invoices.append(invoice)

    return overdue_invoices


def unpaid_total(invoices: list[Invoice]) -> float:

    total = 0.0

    for invoice in invoices:

        if not invoice.paid:
            total += invoice.amount

    return total
