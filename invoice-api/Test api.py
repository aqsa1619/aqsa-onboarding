import pytest
from fastapi.testclient import TestClient

from main import app, get_data_path


@pytest.fixture
def client(tmp_path):
    """Each test gets its own empty temp file, so tests never touch invoices.json."""
    data_file = tmp_path / "invoices.json"
    app.dependency_overrides[get_data_path] = lambda: str(data_file)
    yield TestClient(app)
    app.dependency_overrides.clear()


def make(client, name="Acme", amount=100.0, due="2026-12-01"):
    return client.post(
        "/api/invoices", json={"client": name, "amount": amount, "due_date": due}
    )


def test_health(client):
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_list_empty_then_filled(client):
    assert client.get("/api/invoices").json() == []
    make(client)
    assert len(client.get("/api/invoices").json()) == 1


def test_create_returns_201_and_invoice_out(client):
    r = make(client, "Globex", 250.5)
    assert r.status_code == 201
    assert r.json() == {
        "id": 1, "client": "Globex", "amount": 250.5,
        "due_date": "2026-12-01", "paid": False,
    }


def test_get_by_id(client):
    make(client)
    r = client.get("/api/invoices/1")
    assert r.status_code == 200
    assert r.json()["client"] == "Acme"


def test_404_when_missing(client):
    r = client.get("/api/invoices/999")
    assert r.status_code == 404
    assert "999" in r.json()["detail"]


def test_422_on_negative_amount(client):
    r = make(client, amount=-5)
    assert r.status_code == 422
    assert "amount" in str(r.json()["detail"])


def test_422_on_missing_due_date(client):
    r = client.post("/api/invoices", json={"client": "Acme", "amount": 10})
    assert r.status_code == 422


def test_422_on_empty_client(client):
    assert make(client, name="").status_code == 422


def test_report_route_not_swallowed_by_id(client):
    make(client, "A", 10)
    make(client, "B", 20)
    r = client.get("/api/invoices/report")
    assert r.status_code == 200
    assert r.json()["count"] == 2


def test_cors_header_for_localhost_3000(client):
    r = client.get("/api/health", headers={"Origin": "http://localhost:3000"})
    assert r.headers["access-control-allow-origin"] == "http://localhost:3000"