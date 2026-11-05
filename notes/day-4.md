# Day 4: FastAPI Invoice API Verification

## Summary of Tasks
* **Setup**: Initialized `invoice-api/` with dedicated `.venv` and `requirements.txt`.
* **Integration**: Connected backend modules (`models.py`, `schemas.py`, `store.py`, `report.py`) with `main.py`.
* **Bug Fixes**: Resolved file path argument issues in `store.py` and Pydantic attribute mismatches.

---

## Endpoint Verification Log (Swagger UI)

### 1. GET `/api/health`
* **Status**: `200 OK`
* **Details**: Confirms server status (`{"status": "ok"}`).
![Health Check](./notes/api-health.jpg)

### 2. GET `/api/invoices`
* **Status**: `200 OK`
* **Details**: Loads and lists stored JSON invoice records.
![List Invoices](./notes/get-api-invoices.jpg)

### 3. POST `/api/invoices`
* **Status**: `201 Created`
* **Details**: Validates payload via Pydantic schemas and saves to `invoices.json`.
![Create Invoice](./notes/post-api-invoices.jpg)

### 4. GET `/api/invoices/{id}`
* **Status**: `200 OK` (Found) 
* **Details**: Fetches specific record by ID.
![GET Invoice 404 Error](./notes/invoices{id}.jpg)

### 5. GET `/api/invoices/report`
* **Status**: `200 OK`
* **Details**: Computes financial metrics (counts, totals, paid vs. unpaid).
![Invoice Report](./notes/invoices-report.jpg)

### 6. Next.js Frontend (`/invoices`)
- **Status**: `200 OK`
- **Details**: Successfully connects to FastAPI backend via CORS and renders live Python records in a table component.
![Next.js Invoices Table](./notes/nextjs-invoices.jpg)

### 6. Next.js Invoices Table & Form (`/invoices`)
- **Status**: `200 OK` & `422 Unprocessable Entity` Handled
- **Details**: Successfully connects to FastAPI via CORS, displays live records[cite: 7, 8], handles successful `POST` submissions with paid status[cite: 7, 8], and catches/displays FastAPI validation errors on the UI[cite: 9].

**Success State (Invoice Created & Paid Status):**
![Invoice Form Success](./notes/invoice-form-success.jpg)

**Validation Error State (422 Error Handling):**
![Invoice Form 422 Error](./notes/invoice-form-error.jpg)