# Part A: Project Structure & Basics

* **`package.json`**: Acts as the project's recipe card. It lists installed packages and defines shortcut scripts:
    `dev` starts the local dev server
    `build` compiles code for production
    `start` runs the production build
    `lint` checks for code errors.
* **`src/app/`**: The core directory of the App Router; any folder created inside it automatically becomes a working URL route (provided it contains a `page.tsx` file).
* **`src/app/layout.tsx`**: The global root layout that wraps around every page in the application, ensuring shared UI elements (like global fonts or HTML tags) are present everywhere.
* **`src/app/page.tsx`**: Corresponds directly to the root URL (`/`), which serves as the main homepage of the website (`http://localhost:3000/`).
* **`src/app/globals.css`**: Imported directly into the root layout to bring in Tailwind CSS and apply global styling rules site-wide.
* **`public/`**: Stores static assets (like images) that are served directly from the root URL and can be referenced instantly in the browser (e.g., `/next.svg`).
* **`next.config.ts`**: The configuration file where global Next.js framework settings and custom options are defined.
* **`tsconfig.json`**: Configures TypeScript compiler settings and defines path aliases (such as `@/*` pointing to `./src/*`) to shorten imports and avoid messy relative paths like `../../../`.
* **`.gitignore`**: Specifies files and folders—such as `node_modules/` (heavy packages) and `.env` (sensitive security keys)—that must be excluded from Git version control.