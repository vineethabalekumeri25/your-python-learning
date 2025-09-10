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


if __name__ == "__main__":
    create_table()
    insert_user("Alice", 25)
    insert_user("Bob", 30)
    print("Users:", fetch_users())
