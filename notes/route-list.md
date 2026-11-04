When we run `npm run build`, Next.js checks every page and splits them into two types:

- **Static Routes (`○`)** — These pages never change, so they are built once into fast HTML files ahead of time:
  - `/` (Home page)
  - `/_not-found` (Error page)
  - `/about` (About page)
  - `/admin` (Admin page)
  - `/api/hello` (API route)
  - `/services` (Services list page)
  - `/tasks` (Task tracker page)

- **Dynamic Server / Partial Prerender Routes (`ƒ` / `◐`)** — Pages or API routes that render dynamically on request or handle route parameters:
  - `/api/tasks` (Dynamic backend API route for tasks)
  - `/services/[slug]` (Individual service detail pages)

---
*Reference screenshot saved in `notes/route-list.png` directory.*