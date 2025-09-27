"""
Basic SQLite Example
"""

import sqlite3


def create_table():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()
    conn.close()


def insert_user(name, age):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()


def fetch_users():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_user(user_id, new_name, new_age):
    """Update a user by ID"""
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (new_name, new_age, user_id))
    conn.commit()
    conn.close()


def delete_user(user_id):
    """Delete a user by ID"""
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_user("Alice", 25)
    insert_user("Bob", 30)
    insert_user("Charlie", 28)

    print("Users:", fetch_users())
    print("Before Update/Delete Users:", fetch_users())

# Update user (e.g., change Bob’s info)
    update_user(2, "Bobby", 35)

        # Delete user (e.g., remove Charlie)
    delete_user(3)

    print("After Update/Delete:", fetch_users())
