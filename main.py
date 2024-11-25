from user_manager import UserManager
from cart import Cart
from product import ProductManager


def main():
    user_manager = UserManager()
    product_manager = ProductManager()
    cart = Cart()

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            user_manager.register()
        elif choice == "2":
            username = user_manager.login()
            print(f"Welcome, {username}!")

            while True:
                print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Logout")
                user_choice = input("Select an option: ")

                if user_choice == "1":
                    product_manager.display_products()
                elif user_choice == "2":
                    product_manager.display_products()
                    product_name = input("Enter the product name to add to cart: ")
                    product = product_manager.find_product(product_name)
                    if product:
                        quantity = int(input(f"Enter quantity for {product.name} (Available: {product.stock}): "))
                        if product.reduce_stock(quantity):
                            cart.add_to_cart(product, quantity)
                        else:
                            print("Insufficient stock!")
                    else:
                        print("Product not found.")
                elif user_choice == "3":
                    cart.view_cart()
                elif user_choice == "4":
                    if cart.checkout():
                        break
                elif user_choice == "5":
                    print("Logged out.")
                    break
                else:
                    print("Invalid choice.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()