import sqlite3

try:
    conn = sqlite3.connect(':memory:')
    print("SQLite is working!")
    conn.close()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
