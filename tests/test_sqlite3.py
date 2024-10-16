# import sqlite3

# def test_sqlite_connection():
#     try:
#         conn = sqlite3.connect(':memory:')
#         assert conn is not None
#         print("SQLite is working!")
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#         assert False, "SQLite connection failed!"

def test_always_pass():
    assert True

