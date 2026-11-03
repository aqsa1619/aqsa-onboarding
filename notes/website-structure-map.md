# Part C: Website Structure Map (Beetrix360)

| Path in our repo | Your answer: what it does / which URL |
| :--- | :--- |
| `src/app/layout.tsx` and `src/app/page.tsx` | Global root layout and the homepage rendered at the root URL (`/`). |
| `src/app/[...segments]/page.tsx` | Handles every other page, like /seo or /digital-marketing. It finds the page by its link and shows it. If it doesn't exist, it shows the 404 page. |
| `src/app/not-found.tsx` | The global custom 404 error page displayed when a user visits a route that does not exist. |
| `src/app/admin/login/page.tsx` and `LoginForm.tsx` | The admin login page, at /admin/login. page.tsx is the page itself, and if you're already logged in it sends you to the dashboard. LoginForm.tsx is the email and password form. |
| `src/app/admin/(dashboard)/layout.tsx` and its folders | The frame for all admin pages. It checks you are logged in, and if not, it sends you to the login page. It also shows the side menu. The (dashboard) brackets are only for organizing files, so they don't appear in the link. |
| `src/app/admin/actions.ts` ("use server") | Starts with "use server", which means it runs only on server, never in the visitor's browser. It has no link of its own. It holds all the "save" jobs for the admin: save homepage, save pages, save menu, manage users, log out. |
| `src/app/api/admin/login/route.ts` and `api/admin/upload` | Checks the email and password when someone logs in. If they're right, it keeps the person logged in for 7 days. The link is /api/admin/login. |
| `sitemap.ts`, `robots.ts`, `opengraph-image.tsx`, `icon.svg` | src/app/sitemap.ts -> Makes /sitemap.xml, a list of the site's pages for Google. It only includes pages that are published and meant to be found.
src/app/robots.ts -> Makes /robots.txt. It tells search engines and AI tools what they may visit.
src/app/opengraph-image.tsx -> Makes the preview picture that appears when someone shares a link to the site.
src/app/icon.svg -> The small logo in the browser tab. |
| `src/app/llms.txt/route.ts` | Makes /llms.txt, a simple text summary of the site for AI tools. |
| `src/components/` (admin, home, pages, sections, site) | src/components/admin/ -> Small parts used only in the admin area, like the image upload box.
src/components/home/ -> The homepage sections, like the hero, pillars, and ROI calculator.
src/components/pages/ -> layout for inner pages, with breadcrumbs.
src/components/sections/ -> The building blocks for inner pages, like text, FAQs, steps, and call-to-action.
src/components/site/ -> Parts shared by the whole site, like the menu, footer, logo, and analytics. |
| `src/lib/` and `src/content/` (JSON files) | src/lib/ -> The helper code behind the scenes. It handles the database, login, uploads, redirects, and SEO.
src/content/ -> Ready-made content files (JSON). They hold the site details, homepage text, and page structure. They are used as backup content. |
| `tsconfig.json` `"@/*" -> "./src/*"` | Configures TypeScript path mapping so any import starting with `@/` points directly to the `src/` directory. |