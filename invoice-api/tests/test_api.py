import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"   # must come before importing main

from fastapi.testclient import TestClient

from auth import hash_password
from db import Base, SessionLocal, engine
from db_models import UserRow
from main import app

Base.metadata.create_all(engine)   # make sure the tables exist in test.db

client = TestClient(app)


def get_token():
    """Create a test user (if missing), log in, and return the token."""
    db = SessionLocal()
    if not db.query(UserRow).filter_by(email="test@test.com").first():
        db.add(UserRow(email="test@test.com", password_hash=hash_password("test123")))
        db.commit()
    db.close()

    response = client.post(
        "/api/auth/login",
        json={"email": "test@test.com", "password": "test123"},
    )
    return response.json()["access_token"]


def auth_headers():
    return {"Authorization": f"Bearer {get_token()}"}


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
        "paid": True,
    }
    response = client.post("/api/invoices", json=payload, headers=auth_headers())
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
    # Invalid amount (negative) should give 422 (with a valid token)
    payload = {
        "client": "Bad Client",
        "amount": -10.0,
        "due_date": "2026-12-31",
    }
    response = client.post("/api/invoices", json=payload, headers=auth_headers())
    assert response.status_code == 422