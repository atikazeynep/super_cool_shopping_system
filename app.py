from flask import Flask, request, jsonify
import json
import os
import uuid

app = Flask(__name__)

# Load products
def load_products():
    if os.path.exists('products.json'):
        with open('products.json', 'r') as file:
            return json.load(file)
    return {}

# Load stock
def load_stock():
    if os.path.exists('stock.json'):
        with open('stock.json', 'r') as file:
            return json.load(file)
    else:
        return {product_id: 0 for product_id in products}

# Save stock
def save_stock(stock):
    with open('stock.json', 'w') as file:
        json.dump(stock, file, indent=4)

# Save order
def save_order(order_id, cart, total_cost):
    order = {
        'order_id': order_id,
        'cart': cart,
        'total_cost': total_cost,
        'rating': None,
        'comment': None
    }
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
    else:
        orders = {}
    orders[order_id] = order
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

# Calculate total cost
def calculate_total_cost(cart, products):
    total_cost = 0.0
    for product_id, quantity in cart.items():
        if product_id in products:
            total_cost += products[product_id]['price'] * quantity
    return total_cost

@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.json
    cart = {}
    product_ids = [key for key in data.keys() if key.startswith('productId')]
    quantity_ids = [key for key in data.keys() if key.startswith('quantity')]

    for product_id_key, quantity_id_key in zip(product_ids, quantity_ids):
        product_id = data[product_id_key]
        quantity = int(data[quantity_id_key])
        cart[product_id] = quantity

    products = load_products()
    stock = load_stock()

    # Check stock availability
    for product_id, quantity in cart.items():
        if product_id not in stock or stock[product_id] < quantity:
            return jsonify({'error': f'Not enough stock for product {product_id}'}), 400

    # Deduct stock
    for product_id, quantity in cart.items():
        stock[product_id] -= quantity

    # Save stock
    save_stock(stock)

    # Save order
    order_id = str(uuid.uuid4())
    total_cost = calculate_total_cost(cart, products)
    save_order(order_id, cart, total_cost)

    return jsonify({'message': 'Order submitted successfully!', 'order_id': order_id})

if __name__ == '__main__':
    app.run(debug=True)

