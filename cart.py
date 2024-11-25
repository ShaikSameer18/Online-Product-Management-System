class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        self.items.append((product, quantity))
        print(f"{quantity} x {product.name} added to the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for product, quantity in self.items:
                cost = product.price * quantity
                total += cost
                print(f"{product.name} (₹{product.price} x {quantity}): ₹{cost}")
            print(f"Total: ₹{total}")
        return total

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Add items before checkout.")
            return False

        total = self.view_cart()
        print("\nProceeding to checkout...")
        print(f"Total amount to pay: ₹{total + 100} (including ₹100 delivery cost)")
        print("Order placed successfully!")
        self.items.clear()
        return True
