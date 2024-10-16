import pytest
from your_flask_app import app  # Replace with the actual import

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():  # Ensure the application context is set
            yield client

def test_add_task(client):
    """Test adding a task."""
    # Ensure the database is clean before the test
    with app.app_context():
        conn = sqlite3.connect('todo.db')
        conn.execute('DELETE FROM tasks')  # Clear all tasks
        conn.commit()
        conn.close()

    # Test valid input
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302  # Redirect to index
    assert response.location.endswith('/')

    # Check if the task was added
    with app.app_context():
        conn = sqlite3.connect('todo.db')
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        assert len(tasks) == 1
        assert tasks[0]['task'] == 'Test Task'
        conn.close()
