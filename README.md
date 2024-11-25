This project is a simple command-line-based shopping system built using Python. It includes functionalities for user registration, login, product browsing, cart management, and order placement.

Features
User Management:

New users can register with a unique username, password, and phone number.
Existing users can log in using their credentials.
Product Management:

Browse a list of available products with details like name, price, category, and stock.
Dynamic inventory management reduces stock after a purchase.
Cart System:

Add products to the cart.
View cart details with product-wise subtotal and total cost.
Checkout to place orders.
File Persistence:

User data is stored in a users.csv file.
Inventory is hardcoded into the program, but it can be extended for file-based or database management.



File Structure

project_directory/

├── main.py                                 # Main script to run the application.


├── user_manager.py                         # Handles user registration and login.


├── product.py                              # Manages product-related functionalities.


├── cart.py                                 # Handles cart operations (optional if merged with product.py).


├── users.csv                               # CSV file to store user details.



How to Use
Run the Application:

Execute main.py to start the program.
Main Menu:

Choose between Register, Login, or Exit.
Register:

Enter a unique username, password, and phone number to register.
Login:

Log in using valid credentials.
After login, you can browse products, add items to the cart, view the cart, or checkout.
Browse Products:

View the list of available products with their details.
Cart Operations:

Add items to the cart.
View cart contents.
Proceed to checkout to place your order.
Code Flow
UserManager:

Handles user registration and login functionalities.
Stores and validates user data using a CSV file.
ProductManager:

Manages the product inventory.
Provides methods to display products and find specific items.
Cart:

Allows users to add, view, and checkout items.
Main Script:

Combines all modules into a menu-driven interface for users.
