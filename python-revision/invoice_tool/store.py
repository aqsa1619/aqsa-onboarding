
import json
from models import Invoice
from datetime import date


def save_invoices(path: str, invoices: list[Invoice]) -> None:

    data = []

    for invoice in invoices:
        invoice_data = {
            "client": invoice.client,
            "amount": invoice.amount,
            "due_date": invoice.due_date.isoformat(),
            "paid": invoice.paid
        }

        data.append(invoice_data)

    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def load_invoices(path: str) -> list[Invoice]:

    try:
        with open(path, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON file: {path}"
        ) from error

    invoices = []

    for item in data:
        invoice = Invoice(
            client=item["client"],
            amount=item["amount"],
            due_date=date.fromisoformat(item["due_date"]),
            paid=item["paid"]
        )

        invoices.append(invoice)

    return invoices
