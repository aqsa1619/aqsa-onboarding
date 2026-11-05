from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_list_invoices():
    response = client.get("/api/invoices")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_invoice():
    payload = {
        "client": "Test Client",
        "amount": 500.0,
        "due_date": "2026-12-31",
        "paid": True
    }
    response = client.post("/api/invoices", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["client"] == "Test Client"
    assert data["amount"] == 500.0
    assert data["paid"] is True

def test_get_invoice_not_found():
    # Requesting an excessively high ID that shouldn't exist
    response = client.get("/api/invoices/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Invoice not found"}

def test_create_invoice_validation_error():
    # Sending an invalid amount (negative or zero) to trigger a 422 error
    payload = {
        "client": "Bad Client",
        "amount": -10.0,
        "due_date": "2026-12-31"
    }
    response = client.post("/api/invoices", json=payload)
    assert response.status_code == 422