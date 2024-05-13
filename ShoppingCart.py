class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity, price_per_unit):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'quantity': quantity, 'price_per_unit': price_per_unit}

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calculate_total(self):
        total = 0
        for item_name, item_info in self.items.items():
            total += item_info['quantity'] * item_info['price_per_unit']
        return total

    def display_items(self):
        print("Items in Cart:")
        for item_name, item_info in self.items.items():
            print(f"{item_name}: {item_info['quantity']} x ${item_info['price_per_unit']} each")

# Example usage:
cart = ShoppingCart()
cart.add_item("Apple", 3, 1.50)
cart.add_item("Banana", 2, 0.75)
cart.display_items()
print("Total:", cart.calculate_total())
cart.remove_item("Apple", 1)
cart.display_items()
print("Total:", cart.calculate_total())
