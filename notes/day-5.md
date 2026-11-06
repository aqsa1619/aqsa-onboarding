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

## Notes

- Data now lives in `invoice.db` on disk, so it survives a restart. `store.py` and `invoices.json` are no longer used by the API.
- Run `python -m pytest`, not `pytest`, so the imports work.
- Run `python import_json.py` only once.
- Run `uvicorn` and `pytest` inside `invoice-api`, `npm` inside `nextjs-structure`, and `git` in the repo root.

*Reference screenshot is saved in notes/invoices-list.png and notes/post-invoices.png