# KZ Strategic Dashboard

Flask dashboard that renders executive views from the `strategic_insight.xlsx`
workbook bundled with the project (one worksheet per dashboard section).

## Local development

```bash
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Optional: use a different workbook
set LOCAL_EXCEL_FILE="D:\\data\\custom_dashboard.xlsx"

python app.py
# http://127.0.0.1:5000
```

## Production deployment

### Option A: Gunicorn (Linux/macOS)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app
```

### Option B: Waitress (Windows)
```bash
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 wsgi:app
```

### Option C: Render (free tier)
1. Push to GitHub.
2. On Render: New → Web Service → connect repo.
3. Runtime: Python
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn wsgi:app`
6. Deploy.

## Configuration

| Name | Description |
|------|-------------|
| `LOCAL_EXCEL_FILE` | Path to the Excel workbook (defaults to `strategic_insight.xlsx`) |
| `SHEET_CACHE_TTL` | Cache TTL in seconds (default 30) |

## Repository structure

```
dashboard_app_from_excel/
├── app.py                  # Flask app (debug disabled in production)
├── wsgi.py                 # WSGI entry point
├── requirements.txt        # Pinned dependencies
├── services/
│   └── google_sheets.py
├── templates/
├── static/
└── strategic_insight.xlsx
```
