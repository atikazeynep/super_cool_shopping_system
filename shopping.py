import uuid
import json
import os

# Dummy product data
products = {
    'P001': {'name': 'Product 1', 'price': 10.0, 'category': 'Electronics'},
    'P002': {'name': 'Product 2', 'price': 15.5, 'category': 'Electronics'},
    'P003': {'name': 'Product 3', 'price': 7.25, 'category': 'Book'},
    'P004': {'name': 'Product 4', 'price': 12.0, 'category': 'Book'},
    'P005': {'name': 'Product 5', 'price': 9.0, 'category': 'Book'},
    'P006': {'name': 'Product 6', 'price': 20.0, 'category': 'Games'},
    'P007': {'name': 'Product 7', 'price': 5.5, 'category': 'Games'},
    'P008': {'name': 'Product 8', 'price': 18.75, 'category': 'Automotive'},
    'P009': {'name': 'Product 9', 'price': 11.0, 'category': 'Automotive'},
    'P010': {'name': 'Product 10', 'price': 14.0, 'category': 'Automotive'},
    'P011': {'name': 'Product 11', 'price': 6.75, 'category': 'Automotive'},
    'P012': {'name': 'Product 12', 'price': 13.5, 'category': 'Food'},
    'P013': {'name': 'Product 13', 'price': 22.0, 'category': 'Food'},
    'P014': {'name': 'Product 14', 'price': 19.25, 'category': 'Food'},
    'P015': {'name': 'Product 15', 'price': 8.0, 'category': 'Food'},
}

def search_products(search_query):
    search_query = search_query.lower().strip()
    matched_products = {pid: prod for pid, prod in products.items() if search_query in prod['name'].lower()}
    return matched_products

def filter_products(min_price=None, max_price=None, category=None):
    filtered_products = products.copy()
    
    if min_price is not None:
        filtered_products = {pid: prod for pid, prod in filtered_products.items() if prod['price'] >= min_price}
    if max_price is not None:
        filtered_products = {pid: prod for pid, prod in filtered_products.items() if prod['price'] <= max_price}
    if category:
        filtered_products = {pid: prod for pid, prod in filtered_products.items() if prod['category'].lower() == category.lower()}
    
    return filtered_products


def calculate_total_cost(cart):
    total_cost = 0.0
    for product_id, quantity in cart.items():
        if product_id in products:
            total_cost += products[product_id]['price'] * quantity
    return total_cost

def save_order(order_id, cart, total_cost):
    order = {
        'order_id': order_id,
        'cart': cart,
        'total_cost': total_cost
    }
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
    else:
        orders = {}
    orders[order_id] = order
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

def main():
    print("Welcome to the product order system!")
    cart = {}
    
    while True:
        action = input("Choose an action - Search (s), Filter (f), Add to Cart (a), Done (d): ").lower()
        if action == 'd':
            break
        elif action == 's':
            search_query = input("Enter search term for product name: ")
            results = search_products(search_query)
            print("Search Results:")
            for pid, prod in results.items():
                print(f"{pid}: {prod['name']} - ${prod['price']} - {prod['category']}")
        elif action == 'f':
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            category = input("Enter category (optional): ")
            results = filter_products(min_price, max_price, category)
            print("Filter Results:")
            for pid, prod in results.items():
                print(f"{pid}: {prod['name']} - ${prod['price']} - {prod['category']}")
        elif action == 'a':
            product_id = input("Enter the product ID to add to cart: ")
            if product_id in products:
                quantity = int(input(f"Enter quantity for {products[product_id]['name']}: "))
                if quantity > 0:
                    if product_id in cart:
                        cart[product_id] += quantity
                    else:
                        cart[product_id] = quantity
                else:
                    print("Quantity must be positive.")
            else:
                print("Invalid product ID.")

    if not cart:
        print("No products in the cart. Exiting...")
    else:
        order_id = str(uuid.uuid4())
        total_cost = calculate_total_cost(cart)
        save_order(order_id, cart, total_cost)
        print(f"\nOrder ID: {order_id}")
        print("\nYour cart:")
        for product_id, quantity in cart.items():
            product_name = products[product_id]['name']
            product_price = products[product_id]['price']
            print(f"{product_name} (Product ID: {product_id}) - Quantity: {quantity} - Unit Price: ${product_price:.2f} - Subtotal: ${product_price * quantity:.2f}")

        print(f"\nTotal cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

