import pytest
from pydantic import ValidationError

from schemas import InvoiceIn


def test_valid_invoice_passes():
    invoice = InvoiceIn(client="Acme", amount=100, due_date="2026-12-01")
    assert invoice.client == "Acme"
    assert invoice.amount == 100


def test_zero_amount_fails():
    with pytest.raises(ValidationError):
        InvoiceIn(client="Acme", amount=0, due_date="2026-12-01")


def test_empty_client_fails():
    with pytest.raises(ValidationError):
        InvoiceIn(client="", amount=100, due_date="2026-12-01")