import os
os.environ["DATABASE_URL"] = "sqlite:///./test.db"   # must come before importing main

import pytest
from fastapi.testclient import TestClient

from auth import hash_password
from db import Base, SessionLocal, engine
from db_models import UserRow
from main import app

Base.metadata.create_all(engine)   # make sure the tables exist in test.db
client = TestClient(app)

EMAIL = "auth-test@test.com"
PASSWORD = "secret123"

INVOICE = {
    "client": "Auth Test Client",
    "amount": 250.0,
    "due_date": "2026-12-31",
    "paid": False,
}


@pytest.fixture(autouse=True)
def make_user():
    """Before every test: make sure the test user exists in test.db."""
    db = SessionLocal()
    if not db.query(UserRow).filter_by(email=EMAIL).first():
        db.add(UserRow(email=EMAIL, password_hash=hash_password(PASSWORD), role="editor"))
        db.commit()
    db.close()


def login(email=EMAIL, password=PASSWORD):
    return client.post("/api/auth/login", json={"email": email, "password": password})


def auth_headers():
    token = login().json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# ---------- The three tests from the task ----------

def test_login_works():
    response = login()
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_wrong_password_gives_401():
    response = login(password="wrong-password")
    assert response.status_code == 401
    assert response.json() == {"detail": "Wrong email or password"}


def test_protected_route_needs_token():
    response = client.post("/api/invoices", json=INVOICE)   # no Authorization header
    assert response.status_code == 401


# ---------- Extra tests (they make the demo stronger) ----------

def test_unknown_email_gives_same_401():
    response = login(email="nobody@test.com")
    assert response.status_code == 401
    assert response.json() == {"detail": "Wrong email or password"}


def test_fake_token_is_rejected():
    response = client.post(
        "/api/invoices", json=INVOICE,
        headers={"Authorization": "Bearer this-is-not-a-real-token"},
    )
    assert response.status_code == 401


def test_edited_token_is_rejected():
    token = login().json()["access_token"]
    header, payload, signature = token.split(".")
    # change one character inside the signature, so the "stamp" no longer matches
    broken = signature[:5] + ("A" if signature[5] != "A" else "B") + signature[6:]
    response = client.post(
        "/api/invoices", json=INVOICE,
        headers={"Authorization": f"Bearer {header}.{payload}.{broken}"},
    )
    assert response.status_code == 401


def test_valid_token_creates_invoice():
    response = client.post("/api/invoices", json=INVOICE, headers=auth_headers())
    assert response.status_code == 201
    assert response.json()["client"] == "Auth Test Client"


def test_report_job_needs_token():
    response = client.post("/api/reports")
    assert response.status_code == 401


def test_report_job_is_created_as_queued():
    response = client.post("/api/reports", headers=auth_headers())
    assert response.status_code == 201
    assert response.json()["status"] == "queued"