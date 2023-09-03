import pytest
import time
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_display_time(client):
    response = client.get('/')
    assert b'Current Time in Moscow' in response.data
    assert response.status_code == 200

def test_time_update(client):
    response1 = client.get('/')
    time.sleep(1)
    response2 = client.get('/')

    print(response1)
    print(response2)

    assert response1.data != response2.data