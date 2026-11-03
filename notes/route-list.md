## Build Route Summary

Running `npm run build` successfully compiles the application and categorizes each route into its rendering type:

* **Static Routes (`○`)** — Prerendered as static HTML content for optimal performance:
  * `/` (Home page)
  * `/_not-found` (Global fallback error page)
  * `/about` (About Us page)
  * `/admin` (Admin Portal)
  * `/api/hello` (Backend JSON API route)
  * `/services` (Services listing page)

* **Partial Prerender / Dynamic Routes (`◐`)** — Prerendered as static HTML with dynamic server-streamed parameters:
  * `/services/[slug]` (Dynamic individual service detail pages)

---
*Reference screenshot saved in `notes/route-list.png` directory.*