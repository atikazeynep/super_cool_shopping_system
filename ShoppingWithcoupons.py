class ShoppingCartWithCoupons(ShoppingCart):
    def __init__(self):
        super().__init__()
        self.coupons = {}
        self.item_brands = {}

    def add_coupon(self, coupon_code, discount_percentage):
        if discount_percentage <= 0 or discount_percentage > 100:
            print("Discount percentage must be between 0 and 100.")
            return
        self.coupons[coupon_code] = discount_percentage

    def apply_coupon(self, coupon_code):
        if coupon_code in self.coupons:
            discount_percentage = self.coupons[coupon_code]
            total_discount = self.calculate_total() * (discount_percentage / 100)
            return total_discount
        else:
            print("Coupon not found.")
            return 0

    def set_item_brand(self, item_name, brand):
        self.item_brands[item_name] = brand

    def display_items_with_brands(self):
        print("Items in Cart:")
        for item_name, item_info in self.items.items():
            brand = self.item_brands.get(item_name, "Unknown Brand")
            print(f"{item_name} ({brand}): {item_info['quantity']} x ${item_info['price_per_unit']} each")

# Example usage:
cart_with_coupons = ShoppingCartWithCoupons()
cart_with_coupons.add_item("Apple", 3, 1.50)
cart_with_coupons.add_item("Banana", 2, 0.75)
cart_with_coupons.set_item_brand("Apple", "Apple Inc.")
cart_with_coupons.display_items_with_brands()
print("Total:", cart_with_coupons.calculate_total())

cart_with_coupons.add_coupon("SUMMER2024", 15)
discount = cart_with_coupons.apply_coupon("SUMMER2024")
print(f"Discount applied: ${discount:.2f}")
print("Total after discount:", cart_with_coupons.calculate_total() - discount)
