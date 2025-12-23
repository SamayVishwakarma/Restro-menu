from flask import Flask, render_template, request
from menu_data import menu_items
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)

@app.route('/order', methods=['POST'])
def order():
    order_items = []
    total = 0
    # form fields are named by "category||item"
    for category, items in menu_items.items():
        for name, price in items.items():
            field = f"{category}||{name}"
            qty_str = request.form.get(field)
            try:
                qty = int(qty_str) if qty_str else 0
            except ValueError:
                qty = 0
            if qty > 0:
                line = price * qty
                order_items.append({'name': name, 'qty': qty, 'rate': price, 'line': line})
                total += line
    return render_template('bill.html', order_items=order_items, total=total, now=datetime.now())

