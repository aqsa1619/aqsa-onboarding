## Repository Structure

```text
aqsa-onboarding/
├── nextjs-structure/            # Next.js App Router project directory
│   ├── src/                     # Main App Router source directory
│   │   ├── app/                 # App router routes and global layouts
│   │   │   ├── (marketing)/     # Route group for public pages (about, services, tasks)
│   │   │   │   ├── about/       # /about route
│   │   │   │   ├── services/    # /services & dynamic /services/[slug] routes
│   │   │   │   └── tasks/       # /tasks interactive task list tracker
│   │   │   ├── admin/           # /admin portal route and layout
│   │   │   ├── api/             # Backend API routes (/api/hello, /api/tasks, /api/invoices)
│   │   │   ├── invoices/        # /invoices page (loading, error, table and add-invoice form)
│   │   │   ├── layout.tsx       # Global root layout
│   │   │   ├── page.tsx         # Homepage
│   │   │   └── not-found.tsx    # Global custom 404 fallback page
│   │   ├── components/          # Reusable UI components (Header.tsx, tasks/)
│   │   └── lib/                 # Data models and utility functions
│   │       ├── api.ts           # Typed fetch helper: apiGet<T>(path)
│   │       └── types.ts         # Shared TypeScript types (Task, Invoice)
│   ├── tsconfig.json            # TypeScript alias setup (@/* -> ./src/*)
│   └── package.json             # Next.js dependencies and scripts
├── python-revision/             # Python core exercises and invoice tool
│   ├── invoice_tool/            # CLI Invoice Tool project
│   │   ├── tests/               # Pytest automated test suite
│   │   │   ├── test_invoice_tool.py
│   │   │   └── test_schemas.py  # Pydantic schema tests
│   │   ├── main.py              # CLI entry point (add, list, report)
│   │   ├── models.py            # Data models and structures
│   │   ├── schemas.py           # Pydantic models: InvoiceIn, InvoiceOut
│   │   ├── report.py            # Financial summary generator
│   │   └── store.py             # JSON persistence handler
│   ├── 1_lists_dict.py          # Exercise 1: Lists & dictionary operations
│   ├── 2_list_comprehension.py  # Exercise 2: List comprehension filtering
│   ├── 3_functions.py           # Exercise 3: Typed functions & calculations
│   ├── 4_exceptions.py          # Exercise 4: Raising/catching ValueError exceptions
│   ├── 5_class.py               # Exercise 5: Dataclass definition and methods
│   ├── 6_JSON.py                # Exercise 6: JSON reading and writing
│   ├── 7_main.py                # Exercise 7: Modular imports and execution
│   ├── 8_requests.py            # Exercise 8: External API calls with requests
│   ├── utils.py                 # Shared helper module
│   ├── clients.json             # Sample JSON data file
│   └── requirements.txt         # Python dependencies
├── invoice-api/                 # FastAPI invoice API (Day 4, own venv)
│   ├── tests/
│   │   └── test_api.py          # TestClient tests for the API
│   ├── main.py                  # FastAPI app: endpoints, CORS, dependency
│   ├── models.py                # Invoice dataclass (from invoice_tool)
│   ├── schemas.py               # Pydantic models: InvoiceIn, InvoiceOut
│   ├── store.py                 # JSON persistence handler (from invoice_tool)
│   ├── report.py                # Financial summary generator (from invoice_tool)
│   ├── pytest.ini               # Lets pytest import the project files
│   ├── requirements.txt         # API dependencies (fastapi, uvicorn, httpx, pytest)
│   └── invoices.json            # Created automatically when the first invoice is added
└── notes/                       # Documentation and assessment deliverables
    ├── structure-basics.md      # Core Next.js App Router concept breakdown
    ├── website-structure-map.md # 12-row structural mapping of beetrix360-website (Part C)
    ├── route-list.md            # Production build route summary (Static vs Dynamic)
    ├── route-list.png           # Screenshot of terminal build output
    ├── day-2-react.md           # Day 2 React state, hooks, and architecture notes
    ├── day-4.md                 # Day 4 FastAPI notes and concept answers
    ├── docs.png                 # Screenshot of the API /docs page
    └── form-422.png             # Screenshot of the form showing a 422 error
```

## How to Run Each Part

### 1. Next.js Practice App

Ensure you have Node.js installed, then run the following from the `nextjs-structure/` folder:

```bash
# Move into the Next.js project
cd nextjs-structure

# Install Next.js dependencies
npm install

# Start the local development server
npm run dev
```

Open http://localhost:3000 in your browser to view the application. The interactive task tracker is at `/tasks` and the invoice table is at `/invoices`.

To verify and generate a production build:

```bash
npm run build
```

The route summary from the build is documented in `notes/route-list.md`.

### 2. Python Revision Exercises (`python-revision/`)

Navigate to the Python revision folder, set up your virtual environment, install requirements, and run any exercise script:

```bash
# Move into the python revision directory
cd python-revision

# 1. Create a virtual environment (.venv)
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate    # On macOS/Linux
# .venv\Scripts\activate     # On Windows Command Prompt / PowerShell

# 3. Install required Python packages from requirements.txt
pip install -r requirements.txt

# 4. Run an individual exercise script
python 7_main.py
python 8_requests.py
```
## 3. Python Invoice Tool

A CLI tool for creating and managing invoices with JSON storage, report generation, Pydantic validation, and automated testing.

### Features

- **Add**: Create and store new invoices
- **List**: Display all recorded invoices
- **Report**: Generate summaries and payment totals
- **Validate**: Check invoice data with Pydantic before it is used

### Pydantic Schemas

The schemas live in `python-revision/invoice_tool/schemas.py`:

- `InvoiceIn`: `client` (not empty), `amount` (greater than 0), `due_date` (a valid date)
- `InvoiceOut`: everything in `InvoiceIn`, plus `id` and `paid` (defaults to `False`)

Bad data raises a clear `ValidationError` that names each invalid field.

### Usage

Navigate into the invoice tool directory (with the virtual environment active):

```bash
cd python-revision/invoice_tool

# Run CLI Tool (add, list, report)
python main.py
```

### Run the Tests

```bash
cd python-revision/invoice_tool

# Run automated tests (invoice tool and schema tests)
python -m pytest
```

Use `python -m pytest` rather than plain `pytest` so the `invoice_tool` modules can be imported.

### 4. Invoice API (`invoice-api/`)

A small web API that turns the invoice tool into endpoints the Next.js `/invoices` page can call.

The API has its own virtual environment, separate from `python-revision/`.

```bash
# Move into the API folder
cd invoice-api

# 1. Create and activate its own virtual environment
python3 -m venv .venv
source .venv/bin/activate    # On macOS/Linux
# .venv\Scripts\activate     # On Windows Command Prompt / PowerShell

# 2. Install the API packages
pip install -r requirements.txt

# 3. Start the API on port 8000
uvicorn main:app --reload --port 8000
```

Open http://localhost:8000/docs to try every endpoint in the browser.

To see the whole thing working together, keep two terminals open:

| Terminal | Folder | Command | Address |
|----------|--------|---------|---------|
| 1 | `invoice-api/` | `uvicorn main:app --reload --port 8000` | http://localhost:8000/docs |
| 2 | `nextjs-structure/` | `npm run dev` | http://localhost:3000/invoices |


### Endpoints

| Method | Path | What it does | Success | Errors |
|--------|------|--------------|---------|--------|
| GET | `/api/health` | Check the API is running | 200 | |
| GET | `/api/invoices` | List invoices. Optional filter: `?paid=true` or `?paid=false` | 200 | |
| GET | `/api/invoices/{id}` | Get one invoice | 200 | 404 if it does not exist |
| POST | `/api/invoices` | Add an invoice (`InvoiceIn` in, `InvoiceOut` out) | 201 | 422 if the data is wrong |
| GET | `/api/invoices/report` | Totals: count, total, paid and unpaid amounts | 200 | |

### Run the API Tests

```bash
cd invoice-api
source .venv/bin/activate

# Run the API tests
pytest -q
```

The tests use FastAPI's `TestClient`, so no browser or running server is needed. They cover health, list, create (201), get one, 404, 422 (three cases), the `paid` filter, the report route and the CORS header.

`pytest.ini` in this folder lets plain `pytest` work here, so there is no need for `python -m pytest`.