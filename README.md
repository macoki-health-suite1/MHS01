# MaCoKi Health Suite (MHS)

A clean full-stack foundation for the MaCoKi Health Suite healthcare platform.

## Stack
- Frontend: React + Vite + TypeScript
- Backend: Django + Django REST Framework
- Development database: SQLite
- API: `/api/`
- Development environment: GitHub Codespaces / Dev Container

## Repository contract
This repository contains source code, configuration, migrations, tests, documentation, and reproducible setup files. Runtime data, secrets, dependency directories, and patient uploads are intentionally excluded from Git.

## Fresh setup
```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/manage.py migrate
python backend/manage.py check
cd frontend
npm install
npm run build
```

## Run
Backend:
```bash
source .venv/bin/activate
python backend/manage.py runserver 0.0.0.0:8000
```

Frontend:
```bash
cd frontend
npm run dev -- --host 0.0.0.0
```

## Verification
From the repository root:
```bash
bash scripts/verify.sh
```

The project is intentionally being built in phases. This package establishes the reproducible foundation first; clinical modules are added only after the foundation passes verification.
