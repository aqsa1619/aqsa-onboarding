# Day 3: API calls and checking data

## What I learned

- **GET** reads data. **POST** creates data.
- The server answers with a **status code**:
  - 200 = OK
  - 201 = created
  - 400 = the request could not be read (bad JSON)
  - 422 = the request was read, but the data is wrong
  - 500 = server error
- **JSON** is the text format the browser and server use to talk.
- A page should show **Loading...** while it waits and a **red message** if the call fails.
- A **generic** like `apiGet<Invoice[]>` tells TypeScript what data comes back, so the editor can catch mistakes.
- **Pydantic** checks data before we use it. Wrong data gives a clear error.

## What I built

**Next.js**
- `src/lib/api.ts`: `apiGet<T>` sends a request and throws an error if the status is not OK.
- `src/lib/types.ts`: added the `Invoice` type.
- `src/app/api/invoices/route.ts`: returns 5 made-up invoices.
- `src/app/invoices/page.tsx`: shows Loading..., a table, or a red error.
- `src/app/api/tasks/route.ts`: added `POST` that returns 400, 422 or 201.

**Python**
- `schemas.py`: `InvoiceIn` (client not empty, amount more than 0, valid date) and `InvoiceOut` (adds `id` and `paid`).
- `tests/test_schemas.py`: 3 tests (valid passes, amount 0 fails, empty client fails).

## How I checked it

- `npm run build` passes and `/invoices` shows in the route list.
- I tested all 3 states on `/invoices`: Loading..., table, and the red error (by forcing a 500).
- I tested `POST /api/tasks` with `curl -i`:
  - `{"title":"ab"}` gave 422
  - `{"title":"Write docs"}` gave 201
  - `not json` gave 400
Reference screenshot saved in `notes/status-code.png` directory
- `python -m pytest` passes.

## Notes

- The server does not save tasks. There is no database, so `/tasks` keeps its list in `localStorage`.
- Use `python -m pytest`, not `pytest`, so the imports work.
- Run `npm` commands in the inner `nextjs-structure` folder and `git` commands in the repo root.