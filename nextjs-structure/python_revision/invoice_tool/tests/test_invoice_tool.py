
from datetime import date

import pytest

from models import Invoice
from store import save_invoices, load_invoices
from report import total_by_client, overdue, unpaid_total


# Test 1: Negative invoice amount should raise ValueError
def test_negative_amount_raises_error():
    with pytest.raises(ValueError):
        Invoice("Test Client", -100, date(2026, 11, 30))


# Test 2: Empty client name should raise ValueError
def test_empty_client_raises_error():
    with pytest.raises(ValueError):
        Invoice("   ", 100, date(2026, 11, 30))


# Test 3: Save and load invoices should preserve the data
def test_save_and_load_invoices(tmp_path):
    invoices = [
        Invoice("Test Client", 2000, date(2026, 11, 30)),
        Invoice("ABC Company", 3000, date(2026, 12, 15), True)
    ]

    path = tmp_path / "invoices.json"

    save_invoices(path, invoices)
    loaded = load_invoices(path)

    assert loaded == invoices


# Test 4: Paid invoices should not appear in overdue list
def test_overdue_ignores_paid_invoices():
    invoices = [
        Invoice("Test Client", 1000, date(2026, 10, 1), True),
        Invoice("ABC Company", 2000, date(2026, 10, 1), False)
    ]

    result = overdue(invoices, date(2026, 11, 3))

    assert len(result) == 1
    assert result[0].client == "ABC Company"


# Test 5: Total should correctly combine invoices of the same client
def test_total_by_client():
    invoices = [
        Invoice("Test Client", 1000, date(2026, 11, 30)),
        Invoice("Test Client", 2000, date(2026, 12, 15))
    ]

    result = total_by_client(invoices)

    assert result == {"Test Client": 3000.0}


# Test 6: Missing JSON file should return an empty list
def test_missing_file_returns_empty_list(tmp_path):
    path = tmp_path / "missing.json"

    result = load_invoices(path)

    assert result == []


# Test 7: Invalid JSON should raise a clear ValueError
def test_broken_json_raises_error(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{invalid json")

    with pytest.raises(ValueError, match="Invalid JSON file"):
        load_invoices(path)


# Test 8: Unpaid total should exclude paid invoices
def test_unpaid_total():
    invoices = [
        Invoice("Test Client", 1000, date(2026, 11, 30), False),
        Invoice("ABC Company", 2000, date(2026, 12, 15), True)
    ]

    result = unpaid_total(invoices)

    assert result == 1000.0
