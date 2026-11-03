When we run `npm run build`, Next.js checks every page and splits them into two types:

- **Static Routes (`○`)** — These pages never change, so they are built once into fast HTML files ahead of time:
  - `/` (Home page)
  - `/_not-found` (Error page)
  - `/about` (About page)
  - `/admin` (Admin page)
  - `/api/hello` (API route)
  - `/services` (Services list page)

- **Dynamic Routes (`◐`)** — This page uses brackets (`[slug]`), meaning it creates different service pages on-the-fly depending on what URL the user visits:
  - `/services/[slug]` (Individual service detail pages)

---
*Reference screenshot saved in `notes/route-list.png` directory.*