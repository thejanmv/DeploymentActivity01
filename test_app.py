from app import app
import sqlite3

def test_add_task():
    """Test adding a task."""
    client = app.test_client()

    # Ensure the database is clean before the test
    conn = sqlite3.connect('todo.db')
    conn.execute('DELETE FROM tasks')  # Clear all tasks
    conn.commit()
    conn.close()

    # Test valid input
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302  # Redirect to index
    assert response.location.endswith(url_for('index'))  # Ensure redirect to home page

    # Verify the task was added
    conn = sqlite3.connect('todo.db')
    tasks = conn.execute('SELECT * FROM tasks WHERE task="Test Task"').fetchall()
    conn.close()
    
    assert len(tasks) == 1  # Ensure the task was added
