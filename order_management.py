import datetime


def update_order_status(order_id, new_status):
    """
    Update the status of an existing order.

    Args:
        order_id (str): The ID of the order to update.
        new_status (str): The new status of the order (e.g., 'pending', 'shipped', 'delivered').
    """
    # Load existing orders from orders.json
    with open('orders.json', 'r') as file:
        orders = json.load(file)

    if order_id in orders:
        orders[order_id]['status'] = new_status
        with open('orders.json', 'w') as file:
            json.dump(orders, file, indent=4)
        print(f"Order {order_id} status updated to '{new_status}'")
    else:
        print(f"Order {order_id} not found")


def get_order_history(customer_id, start_date=None, end_date=None):
    """
    Get the order history for a specific customer within a date range.

    Args:
        customer_id (str): The ID of the customer.
        start_date (datetime.date, optional): The start date of the date range (inclusive).
        end_date (datetime.date, optional): The end date of the date range (inclusive).

    Returns:
        list: A list of orders for the customer within the specified date range.
    """
    # Load existing orders from orders.json
    with open('orders.json', 'r') as file:
        orders = json.load(file)

    customer_orders = []
    for order in orders.values():
        order_date = datetime.datetime.strptime(order['order_date'], '%Y-%m-%d').date()
        if (not start_date or order_date >= start_date) and (not end_date or order_date <= end_date):
            customer_orders.append(order)

    return customer_orders


def cancel_order(order_id):
    """
    Cancel an existing order.

    Args:
        order_id (str): The ID of the order to cancel.
    """
    # Load existing orders from orders.json
    with open('orders.json', 'r') as file:
        orders = json.load(file)

    if order_id in orders:
        if orders[order_id]['status'] == 'pending':
            orders.pop(order_id)
            with open('orders.json', 'w') as file:
                json.dump(orders, file, indent=4)
            print(f"Order {order_id} has been canceled")
        else:
            print(f"Cannot cancel order {order_id} as it is already {orders[order_id]['status']}")
    else:
        print(f"Order {order_id} not found")
