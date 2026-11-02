page.tsx: This is the homepage of your website (the screen you see when you visit http://localhost:3000).
layout.tsx: This is a wrapper file. Anything you put here (like a navigation bar or footer) stays consistent across all pages.
globals.css: Your global styles file, where Tailwind CSS is loaded.
package.json: Think of this as the "recipe card" for your project. It lists all the packages installed (like React and Tailwind) and contains shortcut commands (like npm run dev to start your server).

"""
dev: starts your local development server
build: compiles and optimizes your code for production deployment
start: run the production build of your sites
lint: checks your code for formatting error 

A folder only becomes a working URL if it contains a file named page.tsx. If you make a folder called about but forget to put a page.tsx inside it, visiting /about will give you a "404 Page Not Found" error.

layout.tsx: a wrapper file anything you put here wil eb visible across all pages

loading.tsx: Automatically shows a loading spinner or skeleton while a page is fetching data.

not-found.tsx: Customizes the 404 error page when someone visits a URL that doesn't exist.

src/app/page.tsx: corresponds to the root URL (/)—which is the main homepage of website (e.g., http://localhost:3000/).

src/app/globals.css:
Because layout.tsx wraps around your entire application, importing globals.css there ensures that your global styles and Tailwind CSS rules are applied to every single page on your website automatically.

It is imported in src/app/layout.tsx, brings in Tailwind CSS for styling, and is used to apply global styles and utility classes site-wide

 public/:
 Files placed here are served directly from the root URL, meaning you can access them by referencing their path directly (e.g., /next.svg).

 next.config.ts:
 That is where Next.js settings go.

tsconfig.json:
 It configures TypeScript compiler options and defines the @/* path alias to map imports directly to the src/ folder, shortening paths and avoiding messy relative paths (like ../../../).


 .gitignore:
 It specifies files and folders like node_modules/ (which are too large and can be regenerated via npm install) and .env (which contain sensitive security credentials and secret keys) that should be excluded from Git version control.
"""


tsconfig.json: The configuration file for TypeScript, which ensures your code is type-safe and catches bugs early.

tailwind.config.ts / postcss.config.mjs: Configuration for Tailwind CSS, a styling framework that lets you design web pages quickly using pre-made class names (like bg-blue-500 or text-center).