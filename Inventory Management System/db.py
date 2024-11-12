# db.py
import sqlite3

# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row  # Ensures result rows can be accessed like a dictionary
    return conn
