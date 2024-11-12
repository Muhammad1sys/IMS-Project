# inventory.py
import sqlite3
from db import connect_db

def add_product(name, description, quantity, price):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Products (name, description, quantity, price) VALUES (?, ?, ?, ?)",
                       (name, description, quantity, price))
        conn.commit()
        print("Product added successfully.")
    except sqlite3.Error as e:
        print(f"Failed to add product: {e}")
    finally:
        conn.close()

def view_products():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
        return products
    except sqlite3.Error as e:
        print(f"Failed to retrieve products: {e}")
        return []
    finally:
        conn.close()

def update_product(product_id, name=None, description=None, quantity=None, price=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE Products SET name = ? WHERE id = ?", (name, product_id))
        if description:
            cursor.execute("UPDATE Products SET description = ? WHERE id = ?", (description, product_id))
        if quantity is not None:
            cursor.execute("UPDATE Products SET quantity = ? WHERE id = ?", (quantity, product_id))
        if price is not None:
            cursor.execute("UPDATE Products SET price = ? WHERE id = ?", (price, product_id))
        conn.commit()
        print("Product updated successfully.")
    except sqlite3.Error as e:
        print(f"Failed to update product: {e}")
    finally:
        conn.close()

def delete_product(product_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Products WHERE id = ?", (product_id,))
        conn.commit()
        print("Product deleted successfully.")
    except sqlite3.Error as e:
        print(f"Failed to delete product: {e}")
    finally:
        conn.close()
