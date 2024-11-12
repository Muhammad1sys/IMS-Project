# auth.py
import bcrypt

# Function to register a user
def register_user(username, password, role):
    from db import get_db_connection  # Lazy import to avoid circular dependency
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    insert_user_query = '''INSERT INTO users (username, password, role) 
                           VALUES (?, ?, ?)'''
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(insert_user_query, (username, hashed_password, role))
        conn.commit()

# Function to login a user
def login_user(username, password):
    from db import get_db_connection  # Lazy import to avoid circular dependency
    query = '''SELECT password, role FROM users WHERE username = ?'''
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        if result and bcrypt.checkpw(password.encode('utf-8'), result['password'].encode('utf-8')):  # Adjusted 'password' for proper check
            return result['role']  # Return role if login is successful
        else:
            return None  # Return None if login fails
