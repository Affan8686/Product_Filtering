from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data (you can replace with DB later)
products = [
    {"id": 1, "name": "Red Shoes", "price": 1500, "category": "Shoes", "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Blue T-Shirt", "price": 700, "category": "Clothing", "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Smart Watch", "price": 3500, "category": "Accessories", "image": "https://via.placeholder.com/150"},
    {"id": 4, "name": "Black Jeans", "price": 1200, "category": "Clothing", "image": "https://via.placeholder.com/150"},
    {"id": 5, "name": "White Sneakers", "price": 2500, "category": "Shoes", "image": "https://via.placeholder.com/150"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def get_products():
    category = request.args.get('category')
    max_price = request.args.get('max_price')

    filtered = products
    if category:
        filtered = [p for p in filtered if p['category'].lower() == category.lower()]
    if max_price:
        filtered = [p for p in filtered if p['price'] <= int(max_price)]

    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
