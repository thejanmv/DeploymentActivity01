import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_create_task():
    """Test creating a task with valid and invalid data."""
    client = app.test_client()
    
    # Test valid input
    response = client.post('/tasks', data={'title': 'Sample Task'})
    assert response.status_code == 200
    assert b"Task created" in response.data
    
    # Test invalid input (empty title)
    response = client.post('/tasks', data={'title': ''})
    assert response.status_code == 400
    assert b"Error" in response.data



