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
│   │   │   ├── invoices/        # /invoices page (table and add-invoice form, sends the login token)
│   │   │   ├── login/           # /login page (email and password form)
│   │   │   ├── layout.tsx       # Global root layout
│   │   │   ├── page.tsx         # Homepage
│   │   │   └── not-found.tsx    # Global custom 404 fallback page
│   │   ├── components/          # Reusable UI components (Header.tsx, tasks/)
│   │   └── lib/                 # Data models and utility functions
│   │       ├── api.ts           # Fetch helpers: apiGet<T>, login, getToken, logout
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
├── invoice-api/                 # FastAPI invoice API (own venv, SQLite database)
│   ├── tests/
│   │   ├── test_api.py          # TestClient tests for the invoice endpoints
│   │   └── test_auth.py         # Login, token and protected-route tests
│   ├── main.py                  # FastAPI app: routes, CORS, login, invoices, report jobs
│   ├── auth.py                  # bcrypt hashing, JWT creation, current_user dependency
│   ├── db.py                    # Database engine, SessionLocal and get_db (session per request)
│   ├── db_models.py             # Tables: InvoiceRow, UserRow, JobRow
│   ├── models.py                # Invoice dataclass with business rules (amount > 0)
│   ├── schemas.py               # Pydantic models: InvoiceIn, InvoiceOut, LoginIn
│   ├── report.py                # Financial summary generator
│   ├── worker.py                # Background worker that runs queued report jobs
│   ├── seed_user.py             # Creates the first user (run once)
│   ├── import_json.py           # Imports the old invoices.json into the database (run once)
│   ├── store.py                 # Old JSON handler, now used only by import_json.py
│   ├── pytest.ini               # Lets pytest import the project files
│   ├── requirements.txt         # API dependencies
│   ├── .env.example             # Names of the settings, with fake values (copy to .env)
│   └── invoices.json            # Old JSON data, imported once
└── notes/                       # Documentation and assessment deliverables
    ├── structure-basics.md      # Core Next.js App Router concept breakdown
    ├── website-structure-map.md # 12-row structural mapping of beetrix360-website (Part C)
    ├── route-list.md            # Production build route summary (Static vs Dynamic)
    ├── route-list.png           # Screenshot of terminal build output
    ├── day-2-react.md           # Day 2 React state, hooks, and architecture notes
    ├── day-4.md                 # Day 4 FastAPI notes and concept answers
    ├── docs.png                 # Screenshot of the API /docs page
    ├── form-422.png             # Screenshot of the form showing a 422 error
    ├── day-5.md                 # Day 5 database, login and background job notes
    └── task-*.png               # Day 5 screenshots (login 401, token header, job queued/done, tests)
```

Files that are created locally and never committed: `invoice-api/.env` (real secret), `invoice-api/invoice.db` (database) and `invoice-api/test.db` (test database). They are listed in `.gitignore`.

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

Open http://localhost:3000 in your browser to view the application. The interactive task tracker is at `/tasks`, the login page is at `/login` and the invoice table is at `/invoices`.

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

### 3. Python Invoice Tool

A CLI tool for creating and managing invoices with JSON storage, report generation, Pydantic validation, and automated testing.

#### Features

- **Add**: Create and store new invoices
- **List**: Display all recorded invoices
- **Report**: Generate summaries and payment totals
- **Validate**: Check invoice data with Pydantic before it is used

#### Pydantic Schemas

The schemas live in `python-revision/invoice_tool/schemas.py`:

- `InvoiceIn`: `client` (not empty), `amount` (greater than 0), `due_date` (a valid date)
- `InvoiceOut`: everything in `InvoiceIn`, plus `id` and `paid` (defaults to `False`)

Bad data raises a clear `ValidationError` that names each invalid field.

#### Usage

Navigate into the invoice tool directory (with the virtual environment active):

```bash
cd python-revision/invoice_tool

# Run CLI Tool (add, list, report)
python main.py
```

#### Run the Tests

```bash
cd python-revision/invoice_tool

# Run automated tests (invoice tool and schema tests)
python -m pytest
```

Use `python -m pytest` rather than plain `pytest` so the `invoice_tool` modules can be imported.

### 4. Invoice API (`invoice-api/`)

A web API that turns the invoice tool into endpoints the Next.js `/invoices` page can call. Since Day 5 it stores data in a **SQLite database** (through SQLAlchemy), protects invoice creation with **login (bcrypt + JWT)**, and runs report jobs in a **background worker**.

The API has its own virtual environment, separate from `python-revision/`.

#### Setup (first time only)

```bash
# Move into the API folder
cd invoice-api

# 1. Create and activate its own virtual environment
python3 -m venv .venv
source .venv/bin/activate    # On macOS/Linux
# .venv\Scripts\activate     # On Windows Command Prompt / PowerShell

# 2. Install the API packages
python -m pip install -r requirements.txt

# 3. Create your private settings file from the example
cp .env.example .env

# 4. Generate a secret key and paste it into .env as SECRET_KEY
python -c "import secrets; print(secrets.token_hex(32))"

# 5. Create the first user (admin@test.com / admin123, practice login only)
python seed_user.py

# 6. Optional: import the old invoices.json into the database (run once)
python import_json.py
```

`.env` holds the real secret and is never committed. `.env.example` is committed and shows the setting names with fake values:

| Setting | What it is |
|---------|------------|
| `SECRET_KEY` | Long random text used to sign login tokens |
| `DATABASE_URL` | Database address. `sqlite:///./invoice.db` means a file called `invoice.db` in this folder |

The database file `invoice.db` is created automatically the first time the API starts.

#### Start everything

Keep three terminals open:

| Terminal | Folder | Command | Address |
|----------|--------|---------|---------|
| 1 | `invoice-api/` | `uvicorn main:app --reload --port 8000` | http://localhost:8000/docs |
| 2 | `invoice-api/` | `python worker.py` | runs report jobs (needed only for reports) |
| 3 | `nextjs-structure/` | `npm run dev` | http://localhost:3000/invoices |

Open http://localhost:8000/docs to try every endpoint in the browser. For protected endpoints, log in with `POST /api/auth/login`, copy the `access_token`, click **Authorize** and paste it.

#### How login works

1. `POST /api/auth/login` checks the email and password. Passwords are stored only as bcrypt hashes.
2. If they match, the API returns a signed **JWT** that expires after 60 minutes.
3. The Next.js app keeps the token in `localStorage` and sends it as `Authorization: Bearer <token>`.
4. The `current_user` dependency checks the signature and expiry. A missing, edited or expired token gives **401**.

#### How report jobs work

1. `POST /api/reports` saves a job with status `queued` and returns straight away.
2. `worker.py` (a separate program) finds the oldest queued job, sets it to `running`, builds the report, saves the result and sets `done` (or `failed` on error).
3. `GET /api/reports/{id}` shows the current status and, when finished, the result.

If the worker is not running, jobs stay `queued`.

#### Endpoints

| Method | Path | What it does | Needs token | Success | Errors |
|--------|------|--------------|-------------|---------|--------|
| GET | `/api/health` | Check the API is running | No | 200 | |
| POST | `/api/auth/login` | Log in with email and password, returns a token | No | 200 | 401 wrong email or password |
| GET | `/api/invoices` | List invoices | No | 200 | |
| GET | `/api/invoices/{id}` | Get one invoice | No | 200 | 404 if it does not exist |
| POST | `/api/invoices` | Add an invoice (`InvoiceIn` in, `InvoiceOut` out) | **Yes** | 201 | 401 no or bad token, 422 if the data is wrong |
| GET | `/api/invoices/report` | Totals: count, total, paid and unpaid amounts (calculated inside the request) | No | 200 | |
| POST | `/api/reports` | Create a report job (status `queued`) | **Yes** | 201 | 401 |
| GET | `/api/reports/{id}` | Show a job's status and result | **Yes** | 200 | 401, 404 if the job does not exist |

#### Database tables

| Table | Columns |
|-------|---------|
| `invoices` | `id` (primary key), `client`, `amount`, `due_date`, `paid` |
| `users` | `id` (primary key), `email` (unique), `password_hash`, `role` (`admin` or `editor`) |
| `jobs` | `id` (primary key), `status`, `result`, `user_id` (foreign key to `users`), `created_at` |

To look at the data:

```bash
sqlite3 invoice.db "select * from invoices;"
sqlite3 invoice.db "select id, status, user_id from jobs;"
```

#### Run the API Tests

```bash
cd invoice-api
source .venv/bin/activate

# Run the API tests
python -m pytest -v
```

The tests use FastAPI's `TestClient`, so no browser or running server is needed. They run against a separate `test.db`, so real data is never touched.

- `tests/test_api.py`: health, list, create (201, with a token), 404 and 422.
- `tests/test_auth.py`: login works, wrong password gives 401, a protected route needs a token, an unknown email, a fake token and an edited token are rejected, and a new report job starts as `queued`.
- delete the old test database with `rm -f test.db` and run the tests again.