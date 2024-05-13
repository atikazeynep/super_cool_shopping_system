def apply_festival_discount(cart):
    festival_items = ["Cake", "Decoration", "Gifts"]
    for item_name in festival_items:
        if item_name in cart.items:
            cart.items[item_name]['price_per_unit'] *= 0.9  # 10% discount for festival items

# Create a shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item("Cake", 1, 20)  # Cake for the festival
cart.add_item("Decoration", 2, 5)  # Decorations for the festival
cart.add_item("Book", 1, 15)  # Regular item
cart.add_item("Gifts", 3, 10)  # Gifts for the festival

# Apply festival discount
apply_festival_discount(cart)

# Display items and total
print("Items in Cart:")
for item_name, item_info in cart.items.items():
    print(f"{item_name}: {item_info['quantity']} x ${item_info['price_per_unit']} each")
print("Total:", cart.calculate_total())
