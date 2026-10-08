#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 -m py_compile $(find backend -name '*.py' -type f)
python3 backend/manage.py check
python3 backend/manage.py makemigrations --check --dry-run
if command -v npm >/dev/null 2>&1; then
  cd frontend
  npm run build
fi
echo 'MHS verification passed.'
