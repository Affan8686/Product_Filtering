from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data (you can replace with DB later)
products = [
    {"id": 1, "name": "Red Shoes", "price": 1500, "category": "Shoes", "image": "./static/assets/shopping.webp"},
    {"id": 2, "name": "Blue T-Shirt", "price": 700, "category": "Clothing", "image": "./static/assets/shopping (1).webp"},
    {"id": 3, "name": "Smart Watch", "price": 3500, "category": "Accessories", "image": "./static/assets/Watch.webp"},
    {"id": 4, "name": "Black Jeans", "price": 1200, "category": "Clothing", "image": "./static/assets/shopping (3).webp"},
    {"id": 5, "name": "White Sneakers", "price": 2500, "category": "Shoes", "image": "./static/assets/shopping (4).webp"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def get_products():
    category = request.args.get('category')
    max_price = request.args.get('max_price')
    search_query = request.args.get('q', '').lower()

    filtered = products
    if category:
        filtered = [p for p in filtered if p['category'].lower() == category.lower()]
    if max_price:
        filtered = [p for p in filtered if p['price'] <= int(max_price)]
    if search_query:
        filtered = [p for p in filtered if search_query in p['name'].lower()]

    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
