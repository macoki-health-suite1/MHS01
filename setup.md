# Setup

1. Copy `.env.example` to `.env`.
2. Install backend dependencies with `pip install -r backend/requirements.txt`.
3. Run `python backend/manage.py migrate`.
4. Run `python backend/manage.py check`.
5. Install frontend dependencies with `cd frontend && npm install`.
6. Run `npm run build`.

Do not commit `.env`, databases, `node_modules`, or patient uploads.
