# auth.py
import bcrypt
import sqlite3
from db import connect_db

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(hashed, password):
    return bcrypt.checkpw(password.encode(), hashed)

def register_user(username, password, role='user'):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)",
                       (username, hash_password(password), role))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    except sqlite3.Error as e:
        print(f"Failed to register user: {e}")
    finally:
        conn.close()

def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, password, role FROM Users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user and check_password(user[1], password):
            print("Login successful!")
            return {'id': user[0], 'role': user[2]}
        else:
            print("Invalid username or password.")
            return None
    except sqlite3.Error as e:
        print(f"Login failed: {e}")
        return None
    finally:
        conn.close()
