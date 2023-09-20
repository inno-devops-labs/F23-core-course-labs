import pytest

from ..scripts.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_show_moscow_time(client):
    response = client.get('/')
    assert b"Current Moscow Time" in response.data
    assert response.status_code == 200
    assert b"2023" in response.data  # Update this with the current year
