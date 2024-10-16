import pytest
from app import app  

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test if the home page returns a 200 status code."""
    response = client.get('/')
    assert response.status_code == 200
