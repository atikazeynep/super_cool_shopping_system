import json
import os

def get_order_details(order_id):
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
            if order_id in orders:
                return orders[order_id]
    return None

def main():
    order_id = input("Enter your order ID to check the status: ").strip()
    order_details = get_order_details(order_id)
    
    if order_details:
        print(f"\nOrder ID: {order_details['order_id']}")
        print("Your cart:")
        for product_id, quantity in order_details['cart'].items():
            print(f"{product_id} - Quantity: {quantity}")
        print(f"Total cost: ${order_details['total_cost']:.2f}")
    else:
        print("Order ID not found. Please check and try again.")

if __name__ == "__main__":
    main()

