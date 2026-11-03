# Part C: Website Structure Map (Beetrix360)

| Path in our repo | Your answer: what it does / which URL |
| :--- | :--- |
| `src/app/layout.tsx` and `src/app/page.tsx` | Global root layout and the homepage rendered at the root URL (`/`). |
| `src/app/[...segments]/page.tsx` | Not sure |
| `src/app/not-found.tsx` | The global custom 404 error page displayed when a user visits a route that does not exist. |
| `src/app/admin/login/page.tsx` and `LoginForm.tsx` | Not sure |
| `src/app/admin/(dashboard)/layout.tsx` and its folders | Not sure |
| `src/app/admin/actions.ts` ("use server") | Not sure |
| `src/app/api/admin/login/route.ts` and `api/admin/upload` | Not sure |
| `sitemap.ts`, `robots.ts`, `opengraph-image.tsx`, `icon.svg` | Not sure |
| `src/app/llms.txt/route.ts` | Not sure |
| `src/components/` (admin, home, pages, sections, site) | Not sure |
| `src/lib/` and `src/content/` (JSON files) | Not sure |
| `tsconfig.json` `"@/*" -> "./src/*"` | Configures TypeScript path mapping so any import starting with `@/` points directly to the `src/` directory. |