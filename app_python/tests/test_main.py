import pytest
from main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_current_time(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Current time in Moscow:' in response.data
