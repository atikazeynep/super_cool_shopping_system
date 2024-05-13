import json
import os

def load_products():
    if os.path.exists('products.json'):
        with open('products.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def save_products(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)

def add_product(products):
    product_id = input("Enter the product ID: ").strip()
    if product_id in products:
        print(f"Product ID {product_id} already exists. Please try again.")
        return

    product_name = input("Enter the product name: ").strip()
    try:
        product_price = float(input("Enter the product price: ").strip())
        if product_price < 0:
            print("Price cannot be negative. Please try again.")
            return
    except ValueError:
        print("Invalid price. Please enter a valid number.")
        return

    try:
        product_stock = int(input("Enter the initial stock quantity: ").strip())
        if product_stock < 0:
            print("Stock quantity cannot be negative. Please try again.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a valid integer.")
        return

    products[product_id] = {'name': product_name, 'price': product_price, 'stock': product_stock}
    print(f"Added {product_name} (Product ID: {product_id}) to the system.")

def main():
    products = load_products()
    while True:
        print("\nProduct Management Menu:")
        print("1. Add new product")
        print("2. View all products")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_product(products)
            save_products(products)
        elif choice == '2':
            print("\nCurrent products:")
            for product_id, details in products.items():
                print(f"ID: {product_id}, Name: {details['name']}, Price: ${details['price']:.2f}, Stock: {details['stock']}")
        elif choice == '3':
            save_products(products)
            print("Exiting product management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

