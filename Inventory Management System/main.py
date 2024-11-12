# main.py
from auth import register_user, login_user
from inventory import Inventory, Product
from utils import validate_price, validate_quantity, format_price
from db import get_db_connection

# Function to create the user table
def create_user_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    );
    '''
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()

# Function to create the product table
def create_product_table():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    );
    '''
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()

def admin_menu(inventory):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            product_quantity = int(input("Enter product quantity: "))
            price_input = input("Enter product price: ")

            # Validate price
            price = validate_price(price_input)
            if price is None:
                print("Invalid price input. Product not added.")
                continue  # Skip this iteration if price validation fails

            # Format price for display
            formatted_price = format_price(price)
            print(f"Formatted price: {formatted_price}")

            # Create product after validation
            product = Product(len(inventory.products) + 1, product_name, product_description, price, product_quantity)
            inventory.add_product(product)
            print(f"Product '{product_name}' added successfully!")

        elif choice == "2":
            products = inventory.get_all_products()
            for product in products:
                print(product.to_dict())

        elif choice == "3":
            product_id = int(input("Enter product ID to update: "))
            product = inventory.get_product(product_id)
            if product:
                new_quantity = int(input(f"Enter new quantity for '{product.name}': "))
                product.update_stock(new_quantity)
                print(f"Product '{product.name}' updated successfully!")
            else:
                print("Product not found.")

        elif choice == "4":
            product_id = int(input("Enter product ID to delete: "))
            inventory.delete_product(product_id)
            print("Product deleted successfully!")

        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    inventory = Inventory()

    # Create tables if they don't exist
    create_user_table()
    create_product_table()

    while True:
        print("\nWelcome to the Inventory Management System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/user): ")
            register_user(username, password, role)
            print("User registered successfully!")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = login_user(username, password)

            if role:
                print(f"Welcome back, {username}!")
                if role == "admin":
                    admin_menu(inventory)
                else:
                    print("User menu is under development.")
            else:
                print("Invalid login details. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
