import sqlite3
from app import app  # Replace with the actual import

def test_add_task(client):
    # Clear the database
    with app.app_context():
        conn = sqlite3.connect('todo.db')  # Make sure the database file path is correct
        conn.execute('DELETE FROM tasks')
        conn.commit()
        conn.close()  # Close the connection after use

    # Add a task and check the response
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302  # Check for redirect
