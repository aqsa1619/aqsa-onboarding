# Day 4: FastAPI Invoice API & Full-Stack Integration

## Summary of Tasks
- **Setup**: Initialized `invoice-api/` with a dedicated `.venv` and `requirements.txt`.
- **Backend Integration**: Connected modules (`models.py`, `schemas.py`, `store.py`, `report.py`) into `main.py` to serve core endpoints (`/api/health`, `/api/invoices`, `/api/invoices/{id}`, `/api/invoices/report`).
- **CORS Configuration**: Configured `CORSMiddleware` in FastAPI allowing origin `http://localhost:3000`.
- **Frontend Integration & Form**: Connected Next.js `/invoices` to the Python API, implemented invoice creation with `POST`, correctly mapped the `paid` boolean status, and added UI notifications for `422` validation errors.
- **Automated Testing**: Built a `pytest` suite in `tests/test_api.py` using `TestClient`, covering health, list, create, 404, and 422 scenarios with all 5 tests passing.

---

## Endpoint Verification Log (Swagger UI)

### 1. GET `/api/health`
- **Status**: `200 OK`
- **Details**: Confirms server status (`{"status": "ok"}`).
![Health Check](./notes/api-health.jpg)

### 2. GET `/api/invoices`
- **Status**: `200 OK`
- **Details**: Loads and lists stored JSON invoice records.
![List Invoices](./notes/get-api-invoices.jpg)

### 3. POST `/api/invoices`
- **Status**: `201 Created`
- **Details**: Validates payload via Pydantic schemas and saves to `invoices.json`.
![Create Invoice](./notes/post-api-invoices.jpg)

### 4. GET `/api/invoices/{id}`
- **Status**: `200 OK` (Found) / `404 Not Found`
- **Details**: Fetches specific record by ID.
![GET Invoice](./notes/invoices{id}.jpg)

### 5. GET `/api/invoices/report`
- **Status**: `200 OK`
- **Details**: Computes financial metrics (counts, totals, paid vs. unpaid).
![Invoice Report](./notes/invoices-report.jpg)

---

## Full-Stack Integration & Form Verification

### 6. Next.js Invoices Table & Form (`/invoices`)
- **Status**: `200 OK` & `422 Unprocessable Entity` Handled
- **Details**: Successfully connects to FastAPI via CORS, displays live records in a table, handles `POST` submissions with paid status, and displays FastAPI validation errors directly on the page.

**Success State (Invoice Created & Paid Status):**
![Invoice Form Success](./notes/invoice-form-success.png)

**Validation Error State (422 Error Handling):**
![Invoice Form 422 Error](./notes/invoice-form-error.png)

---

## Automated Test Suite (`tests/test_api.py`)
- **Framework**: `pytest` + `TestClient`
- **Result**: `5 passed in 0.84s`
- **Coverage**:
  1. `test_health_check`: Verifies `GET /api/health` returns status `200` and `{"status": "ok"}`.
  2. `test_list_invoices`: Verifies `GET /api/invoices` returns status `200` and a list.
  3. `test_create_invoice`: Verifies `POST /api/invoices` creates an invoice and returns status `201`.
  4. `test_get_invoice_not_found`: Verifies requesting a non-existent ID returns status `404`.
  5. `test_create_invoice_validation_error`: Verifies invalid payloads trigger a status `422`.

---
