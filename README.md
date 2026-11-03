## 📁 Repository Structure

aqsa-onboarding/
├── src/                          # Main Next.js App Router source directory
│   ├── app/                      # App router routes and global layouts
│   │   ├── (marketing)/          # Route group for public pages (about, services, tasks)
│   │   │   ├── about/            # /about route
│   │   │   ├── services/         # /services & dynamic /services/[slug] routes
│   │   │   └── tasks/            # /tasks interactive task list tracker
│   │   ├── admin/                # /admin portal route and layout
│   │   ├── api/                  # Backend API routes (/api/hello, /api/tasks)
│   │   ├── layout.tsx            # Global root layout
│   │   ├── page.tsx              # Homepage
│   │   └── not-found.tsx         # Global custom 404 fallback page
│   ├── components/               # Reusable UI components (Header.tsx, tasks/)
│   └── lib/                      # Data models and utility functions (types.ts)
├── notes/                        # Documentation and assessment deliverables
│   ├── structure-basics.md       # Core Next.js App Router concept breakdown
│   ├── website-structure-map.md  # 12-row structural mapping of beetrix360-website (Part C)
│   ├── route-list.md             # Production build route summary (Static vs Dynamic)
│   ├── route-list.png            # Screenshot of terminal build output
│   └── day-2-react.md            # Day 2 React state, hooks, and architecture notes
├── python_revision/              # Python core exercises and utility scripts
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


How to Run Each Part
1. Next.js Practice App (Beetrix Agency)
Ensure you have Node.js installed, then run the following in your root terminal:
# Install Next.js dependencies
npm install

# Start the local development server
npm run dev

Open http://localhost:3000 in your browser to view the application (including the new interactive /tasks page).

To verify and generate a production build:
npm run build

2. Python Revision Exercises (python_revision/)
Navigate to the Python revision folder, set up your virtual environment, install requirements, and run any exercise script:

# Move into the python revision directory
cd python_revision

# 1. Create a virtual environment (.venv)
python3 -m venv .venv

# 2. Activate the virtual environment
source .venv/bin/activate    # On macOS/Linux
# .venv\Scripts\activate     # On Windows Command Prompt / PowerShell

# 3. Install required Python packages from requirements.txt
pip install -r requirements.txt

# 4. How to run an individual exercise script (e.g., main runner script or requests script)
python 7_main.py
python 8_requests.py