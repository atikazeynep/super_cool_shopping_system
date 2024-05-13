import json
import os

def get_order_details(order_id):
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
            if order_id in orders:
                return orders[order_id]
    return None

def update_order_status(order_id, new_status):
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
        
        if order_id in orders:
            orders[order_id]['status'] = new_status
            with open('orders.json', 'w') as file:
                json.dump(orders, file, indent=4)
            return True
    return False

def main():
    print("Order Management System")
    mode = input("Choose mode: Check Status (c) or Update Status (u): ").lower()

    if mode == 'c':
        order_id = input("Enter your order ID to check the status: ").strip()
        order_details = get_order_details(order_id)
        
        if order_details:
            print(f"\nOrder ID: {order_details['order_id']}")
            print("Your cart:")
            for product_id, quantity in order_details['cart'].items():
                print(f"{product_id} - Quantity: {quantity}")
            print(f"Total cost: ${order_details['total_cost']:.2f}")
            print(f"Order Status: {order_details['status']}")
        else:
            print("Order ID not found. Please check and try again.")
    elif mode == 'u':
        order_id = input("Enter the order ID for status update: ").strip()
        new_status = input("Enter new status (pending, shipped, delivered, cancelled): ").strip()
        if update_order_status(order_id, new_status):
            print("Order status updated successfully.")
        else:
            print("Failed to update order status. Check if the order ID is correct.")

if __name__ == "__main__":
    main()
