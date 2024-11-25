class Product:
    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

class ProductManager:
    def __init__(self):
        self.products = [
            Product("iphone", 50000, "mobiles", 100),
            Product("vivo", 45000, "mobiles", 90),
            Product("puma", 4000, "shoes", 190),
            Product("hrx", 5000, "shoes", 100),
            Product("boat", 1500, "airpods", 150),
            Product("oneplus", 5500, "airpods", 150),
            Product("gun", 5500, "toys", 210),
            Product("teddybear", 9500, "toys", 150),
        ]

    def display_products(self):
        print("\nAvailable Products:")
        for product in self.products:
            print(f"- {product.name} ({product.category}): ₹{product.price}, Stock: {product.stock}")

    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None
