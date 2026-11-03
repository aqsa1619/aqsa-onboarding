# Beetrix Agency Onboarding & Training Repository (`aqsa-onboarding`)

This repository contains the completed **Day 1 Assessment & Onboarding Tasks** for Beetrix360. It includes the Next.js practice application ("Beetrix Agency"), technical architecture documentation, website mapping analysis, and Python revision exercises.

---

## Repository Structure

```text
aqsa-onboarding/
├── src/                          # Main Next.js App Router source directory
│   ├── app/                      # App router routes and global layouts
│   │   ├── (marketing)/          # Route group for public pages (about, services)
│   │   │   ├── about/            # /about route
│   │   │   └── services/         # /services & dynamic /services/[slug] routes
│   │   ├── admin/                # /admin portal route and layout
│   │   ├── api/                  # Backend API routes (/api/hello)
│   │   ├── layout.tsx            # Global root layout
│   │   ├── page.tsx              # Homepage
│   │   └── not-found.tsx         # Global custom 404 fallback page
│   ├── components/               # Reusable UI components (e.g., Header.tsx)
│   └── lib/                      # Data models and utility functions (e.g., services.ts)
├── notes/                        # Documentation and assessment deliverables
│   ├── structure-basics.md       # Core Next.js App Router concept breakdown
│   ├── website-structure-map.md  # 12-row structural mapping of beetrix360-website (Part C)
│   ├── route-list.md             # Production build route summary (Static vs Dynamic)
│   ├── route-list.png            # Screenshot of terminal build output
│   └── collaborators-invitation.png # GitHub settings collaborator verification
├── Part_D_Python_Revision/       # Python core exercises and utility scripts
│   ├── 1_lists_dict.py           # Exercise 1: Lists & dictionary operations
│   ├── 2_list_comprehension.py   # Exercise 2: List comprehension filtering
│   ├── 3_functions.py            # Exercise 3: Typed functions & calculations
│   ├── 4_exceptions.py           # Exercise 4: Raising/catching ValueError exceptions
│   ├── 5_class.py                # Exercise 5: Dataclass definition and methods
│   ├── 6_JSON.py                 # Exercise 6: JSON reading and writing
│   ├── 7_main.py                 # Exercise 7: Modular imports and execution
│   ├── 8_requests.py             # Exercise 8: External API calls with requests
│   ├── utils.py                  # Shared helper module
│   ├── clients.json              # Sample JSON data file
│   └── requirements.txt          # Python dependencies
├── tsconfig.json                 # TypeScript alias setup (@/* -> ./src/*)
└── package.json                  # Next.js dependencies and scripts

npm install
npm run dev
Open http://localhost:3000 in your browser to view the application.

To verify and generate a production build:
npm run build