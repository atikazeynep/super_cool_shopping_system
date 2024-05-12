# Dummy product data
products = {
    'P001': {'name': 'Product 1', 'price': 10.0},
    'P002': {'name': 'Product 2', 'price': 15.5},
    'P003': {'name': 'Product 3', 'price': 7.25},
    'P004': {'name': 'Product 4', 'price': 12.0},
    'P005': {'name': 'Product 5', 'price': 9.0},
    'P006': {'name': 'Product 6', 'price': 20.0},
    'P007': {'name': 'Product 7', 'price': 5.5},
    'P008': {'name': 'Product 8', 'price': 18.75},
    'P009': {'name': 'Product 9', 'price': 11.0},
    'P010': {'name': 'Product 10', 'price': 14.0},
    'P011': {'name': 'Product 11', 'price': 6.75},
    'P012': {'name': 'Product 12', 'price': 13.5},
    'P013': {'name': 'Product 13', 'price': 22.0},
    'P014': {'name': 'Product 14', 'price': 19.25},
    'P015': {'name': 'Product 15', 'price': 8.0},
}

def calculate_total_cost(cart):
    total_cost = 0.0
    for product_id, quantity in cart.items():
        if product_id in products:
            total_cost += products[product_id]['price'] * quantity
    return total_cost

def main():
    print("Welcome to the product order system!")
    cart = {}
    
    while True:
        product_id = input("Enter the product ID (or type 'done' to finish): ").strip()
        if product_id.lower() == 'done':
            break
        if product_id not in products:
            print(f"Product ID {product_id} not found. Please try again.")
            continue
        
        try:
            quantity = int(input(f"Enter the quantity for {products[product_id]['name']} (Product ID: {product_id}): ").strip())
            if quantity <= 0:
                print("Quantity should be a positive integer. Please try again.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a positive integer.")
            continue

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

    if not cart:
        print("No products in the cart. Exiting...")
    else:
        total_cost = calculate_total_cost(cart)
        print("\nYour cart:")
        for product_id, quantity in cart.items():
            product_name = products[product_id]['name']
            product_price = products[product_id]['price']
            print(f"{product_name} (Product ID: {product_id}) - Quantity: {quantity} - Unit Price: ${product_price:.2f} - Subtotal: ${product_price * quantity:.2f}")

        print(f"\nTotal cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

