# main.py

# Sample users database (this should ideally be fetched from a database)
users = {
    "ali": {"password": "ali", "role": "admin"},
    "afnan": {"password": "afnan", "role": "user"}
}

# Sample products list (should ideally be managed through a ProductManager)
products = []

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    # Check if user exists and credentials are correct
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return users[username]["role"]
    else:
        print("Invalid credentials")
        return None

def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return
    
    password = input("Enter password: ")
    role = input("Enter role (admin/user): ").lower()
    
    # Add user to users database (could be expanded with password encryption, etc.)
    users[username] = {"password": password, "role": role}
    print(f"User {username} registered successfully.")

def view_products():
    if not products:
        print("No products found.")
    else:
        print("Product List:")
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Stock: {product['stock']}")

def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product quantity: "))
    
    product = {
        "id": len(products) + 1,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }
    products.append(product)
    print(f"Product {name} added successfully.")

def update_product():
    try:
        product_id = int(input("Enter product ID to update: "))
        product = next((p for p in products if p["id"] == product_id), None)
        
        if not product:
            print(f"Product with ID {product_id} not found.")
            return

        new_name = input("Enter new product name (leave blank to skip): ")
        new_category = input("Enter new product category (leave blank to skip): ")
        new_price = input("Enter new product price (leave blank to skip): ")
        new_stock = input("Enter new stock quantity (leave blank to skip): ")
        
        # Update product details if provided
        if new_name:
            product["name"] = new_name
        if new_category:
            product["category"] = new_category
        if new_price:
            product["price"] = float(new_price)
        if new_stock:
            product["stock"] = int(new_stock)
        
        print(f"Product {product_id} updated.")
    except ValueError:
        print("Invalid input. Please enter valid values.")

def delete_product():
    try:
        product_id = int(input("Enter product ID to delete: "))
        product = next((p for p in products if p["id"] == product_id), None)
        
        if product:
            products.remove(product)
            print(f"Product {product_id} deleted.")
        else:
            print(f"Product with ID {product_id} not found.")
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")

def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Logout")
        
        choice = input("Choose an option (1/2/3/4/5): ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu():
    print("\nUser Menu:")
    print("1. View Products")
    print("2. Logout")
    
    while True:
        choice = input("Choose an option (1/2): ")
        
        if choice == "1":
            view_products()
        elif choice == "2":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    print("Welcome to the Inventory Management System!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            role = login()
            if role == "admin":
                admin_menu()
            elif role == "user":
                user_menu()
            else:
                print("Login failed. Please try again.")
        elif choice == "3":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
