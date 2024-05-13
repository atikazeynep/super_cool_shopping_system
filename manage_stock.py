import json
import os

# Dummy product data
products = {
    'P001': 'Product 1',
    'P002': 'Product 2',
    'P003': 'Product 3',
    'P004': 'Product 4',
    'P005': 'Product 5',
    'P006': 'Product 6',
    'P007': 'Product 7',
    'P008': 'Product 8',
    'P009': 'Product 9',
    'P010': 'Product 10',
    'P011': 'Product 11',
    'P012': 'Product 12',
    'P013': 'Product 13',
    'P014': 'Product 14',
    'P015': 'Product 15',
}

def load_stock():
    if os.path.exists('stock.json'):
        with open('stock.json', 'r') as file:
            return json.load(file)
    else:
        return {product_id: 0 for product_id in products}

def save_stock(stock):
    with open('stock.json', 'w') as file:
        json.dump(stock, file, indent=4)

def view_stock(stock):
    print("\nCurrent stock levels:")
    for product_id, quantity in stock.items():
        print(f"{products[product_id]} (Product ID: {product_id}): {quantity}")

def update_stock(stock):
    while True:
        product_id = input("Enter the product ID to update stock (or type 'done' to finish): ").strip()
        if product_id.lower() == 'done':
            break
        if product_id not in products:
            print(f"Product ID {product_id} not found. Please try again.")
            continue
        
        try:
            quantity = int(input(f"Enter the new stock quantity for {products[product_id]} (Product ID: {product_id}): ").strip())
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a non-negative integer.")
            continue

        stock[product_id] = quantity
        print(f"Updated {products[product_id]} (Product ID: {product_id}) to {quantity} units.")

def main():
    stock = load_stock()
    while True:
        print("\nStock Management Menu:")
        print("1. View stock levels")
        print("2. Update stock levels")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            view_stock(stock)
        elif choice == '2':
            update_stock(stock)
            save_stock(stock)
        elif choice == '3':
            save_stock(stock)
            print("Exiting stock management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

