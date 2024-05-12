import json
import os

def get_order_details(order_id):
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
            if order_id in orders:
                return orders[order_id]
    return None

def save_order_details(order_id, order_details):
    if os.path.exists('orders.json'):
        with open('orders.json', 'r') as file:
            orders = json.load(file)
    else:
        orders = {}
    orders[order_id] = order_details
    with open('orders.json', 'w') as file:
        json.dump(orders, file, indent=4)

def main():
    order_id = input("Enter your order ID to check the status: ").strip()
    order_details = get_order_details(order_id)
    
    if order_details:
        print(f"\nOrder ID: {order_details['order_id']}")
        print("Your cart:")
        for product_id, quantity in order_details['cart'].items():
            print(f"{product_id} - Quantity: {quantity}")
        print(f"Total cost: ${order_details['total_cost']:.2f}")
        
        if order_details['rating'] is not None:
            print(f"Rating: {order_details['rating']}/5")
        if order_details['comment'] is not None:
            print(f"Comment: {order_details['comment']}")

        rate_order = input("Would you like to rate and comment on this order? (yes/no): ").strip().lower()
        if rate_order == 'yes':
            while True:
                try:
                    rating = int(input("Enter your rating (1-5): ").strip())
                    if 1 <= rating <= 5:
                        order_details['rating'] = rating
                        break
                    else:
                        print("Rating must be between 1 and 5. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter an integer between 1 and 5.")
            
            comment = input("Enter your comment: ").strip()
            order_details['comment'] = comment

            save_order_details(order_id, order_details)
            print("Thank you for your feedback!")
    else:
        print("Order ID not found. Please check and try again.")

if __name__ == "__main__":
    main()

