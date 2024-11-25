import csv
import os

class UserManager:
    def __init__(self, filename="users.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Username", "Password", "Phone"])

    def register(self):
        print("Welcome to Amazon Registration!")
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)

            user_id = input("Enter your ID: ")
            while True:
                username = input("Enter a username: ")
                if self.is_username_taken(username):
                    print("Username already exists. Try again.")
                else:
                    break

            password = input("Enter a password: ")
            phone = input("Enter your phone number: ")
            writer.writerow([user_id, username, password, phone])
            print("Registration successful!")

    def is_username_taken(self, username):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            return any(row["Username"] == username for row in reader)

    def login(self):
        print("Welcome to Amazon Login!")
        while True:
            username = input("Enter username: ")
            password = input("Enter password: ")

            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                if any(row["Username"] == username and row["Password"] == password for row in reader):
                    print("Login successful!")
                    return username
                else:
                    print("Invalid credentials. Try again.")
