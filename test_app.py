import pytest
from app import app  # Replace with the actual import
import sqlite3

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    # Clear the database
    with app.app_context():
        conn = sqlite3.connect('todo.db')
        conn.execute('DELETE FROM tasks')  # Clear all tasks
        conn.commit()
        conn.close()

    # Add a task and check the response
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302  # Check for redirect
