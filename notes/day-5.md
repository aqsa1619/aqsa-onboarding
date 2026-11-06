# Day 5: Database, login and background jobs

## What I learned

- A **table** holds one kind of thing. A **row** is one item. The **primary key** is its unique id. A **foreign key** points to a row in another table.
- **SQLAlchemy (ORM)** lets me write Python classes instead of SQL. One class is one table, one object is one row.
- A **session** is a basket of changes. `commit` saves them all. `rollback` cancels them all.
- `Depends(get_db)` gives each request its own session and closes it at the end.
- **bcrypt** makes a one-way, salted hash of a password. Only the hash is stored, never the password.
- A **JWT** has a header, a payload (user id, role, expiry) and a signature. Editing the payload breaks the signature, so the token is rejected.
- **Roles** (`admin`, `editor`) are stored on the user and checked in code.
- Secrets go in **`.env`**, which stays out of git. `.env.example` has fake values only.
- A **background job** is saved by the API and run by a separate **worker**. Status goes `queued` → `running` → `done` / `failed`.

## What I built

**Task 1: SQLite with SQLAlchemy (`invoice-api`)**
- `db.py`: engine, `SessionLocal` and `get_db` (one session per request).
- `db_models.py`: `InvoiceRow` table with id, client, amount, due_date, paid.
- `schemas.py`: added `from_attributes=True` so a row can become `InvoiceOut`.
- `main.py`: endpoints now use `db: Session = Depends(get_db)` instead of `store.py`.
- `import_json.py`: one-time import of the old `invoices.json`.
- `tests/test_api.py`: uses `test.db` so tests do not touch real data.

*Reference screenshot is saved in notes/invoices-list.png and notes/post-invoices.png

**Task 2: Login and protected route**
 
Python (`invoice-api`)
- `db_models.py`: added `UserRow` (id, unique email, password_hash, role).
- `auth.py`: `hash_password`, `verify_password`, `create_token` (JWT, 60 minutes) and `current_user`.
- `schemas.py`: added `LoginIn`.
- `main.py`: `POST /api/auth/login` (same 401 message for unknown email and wrong password) and `Depends(current_user)` on `POST /api/invoices`.
- `seed_user.py`: creates the first user (`admin@test.com`, role admin).
- `tests/test_api.py`: logs in to get a token before creating invoices.
Next.js (`nextjs-structure`)
- `src/lib/api.ts`: added `login`, `getToken` and `logout`. The token is stored in `localStorage`.
- `src/app/login/page.tsx`: login form that redirects to `/invoices`.
- `src/app/invoices/page.tsx`: sends the `Authorization: Bearer` header and shows "Please log in first" on 401.

- Create invoice without a token gave **401**.
- Login with a wrong password gave **401**.(notes/task-2-401.png)
- Login with the right password returned an `access_token`.
- Create invoice with the token gave **201**.(notes/task-2-created.png)
- Create invoice with an edited token gave **401**.
- In the browser, the Network tab showed `Authorization: Bearer ...` on the POST request, and Local Storage showed the `token` entry. (notes/task-2-token-header.png)
- After deleting the token, Add Invoice showed the red "Please log in first" message and a 401 in the Network tab.
- `python -m pytest` passes. (notes/tests-passed.png)
Reference screenshots saved in the `notes/` directory


**Task 3: Job table and worker (`invoice-api`)**
- `db_models.py`: added `JobRow` (id, status, result, `user_id` foreign key, created_at). Status starts as `queued`.
- `main.py`: `POST /api/reports` saves a job and returns at once. `GET /api/reports/{id}` shows the status and the result. Both need a token.
- `worker.py`: a separate program. It finds the oldest `queued` job, sets `running`, builds the report with `build_report`, saves the result and sets `done` (or `failed` on error). It waits 2 seconds when there is nothing to do.
- `time.sleep(5)` in the worker makes `running` visible in the demo.


**Task 3**
- `POST /api/reports` returned instantly with status `queued`. ![queued](notes/task-3-queued.png)
- With the worker stopped, `GET /api/reports/1` still showed `queued`.
- A few seconds later the status was `done` with the report result. ![done](notes/task-3-done.png)
- The worker terminal printed `Job 1: running` and `Job 1: done`. ![worker](notes/task-3-runnin.png)

## Notes

- Data now lives in `invoice.db` on disk, so it survives a restart. `store.py` and `invoices.json` are no longer used by the API.
- Only `POST /api/invoices` and the two report routes are protected. The other `GET` routes work without a token.
- `localStorage` is simple but readable by page JavaScript. A production app would often use cookies instead.
- The worker must run in its own terminal, in `invoice-api`, using the same Python environment as the server. If it is not running, jobs stay `queued`.
- Use `python -m pip install ...` so packages go into the same Python that runs the code. Missing `bcrypt` and `fastapi` errors came from the wrong environment.
- Run `python -m pytest`, not `pytest`, so the imports work.
- Run `python import_json.py` and `python seed_user.py` only once.
- Run `uvicorn`, `worker.py` and `pytest` inside `invoice-api`, `npm` inside `nextjs-structure`, and `git` in the repo root.