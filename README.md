# RestroMenu — Web App

This converts the original `RestroMenu.py` script into a small Flask web app.

Quick start:

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

Files added:
- `app.py` — Flask application
- `menu_data.py` — menu data
- `templates/index.html`, `templates/bill.html` — UI
- `static/style.css` — styles

If you want the original console script preserved, `RestroMenu.py` remains unchanged.
