
import argparse
from datetime import date

from models import Invoice
from store import load_invoices, save_invoices
from report import total_by_client, overdue, unpaid_total


DATA_FILE = "invoices.json"


def main() -> None:

    # Create the main argument parser
    parser = argparse.ArgumentParser(
        description="Simple Invoice Management Tool"
    )

    # Create subcommands
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ADD command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new invoice"
    )

    add_parser.add_argument("--client", required=True)
    add_parser.add_argument("--amount", required=True, type=float)
    add_parser.add_argument("--due", required=True)

    # LIST command
    subparsers.add_parser(
        "list",
        help="Display all invoices"
    )

    # REPORT command
    subparsers.add_parser(
        "report",
        help="Generate invoice report"
    )

    # Read arguments from Terminal
    args = parser.parse_args()

    # Load existing invoices
    try:
        invoices = load_invoices(DATA_FILE)
    except ValueError as error:
        print(f"Error: {error}")
        return

    # ADD invoice
    if args.command == "add":

        try:
            due_date = date.fromisoformat(args.due)

            invoice = Invoice(
                client=args.client,
                amount=args.amount,
                due_date=due_date
            )

            invoices.append(invoice)

            save_invoices(DATA_FILE, invoices)

            print("Invoice added successfully!")

        except ValueError as error:
            print(f"Error: {error}")

    # LIST invoices
    elif args.command == "list":

        if not invoices:
            print("No invoices found.")

        else:
            print("\nAll Invoices:")

            for invoice in invoices:
                print(invoice)

    # GENERATE report
    elif args.command == "report":

        print("\nTotals By Client:")

        totals = total_by_client(invoices)

        for client, total in totals.items():
            print(f"{client}: {total:.2f}")

        print(f"\nUnpaid Total: {unpaid_total(invoices):.2f}")

        overdue_invoices = overdue(invoices, date.today())

        print("\nOverdue Invoices:")

        if not overdue_invoices:
            print("No overdue invoices.")

        else:
            for invoice in overdue_invoices:
                print(invoice)


if __name__ == "__main__":
    main()
