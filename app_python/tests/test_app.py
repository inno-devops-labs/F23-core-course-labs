import re
import pytest
import time
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_index_route(client):
    response = client.get('/')
    assert b'Current Time in Moscow' in response.data
    assert response.status_code == 200

def test_get_time_route(client):
    response = client.get('/time')
    assert response.status_code == 200

    assert bool(re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', response.get_data(as_text=True)))

def test_time_update(client):
    response1 = client.get('/')
    time.sleep(1)
    response2 = client.get('/')

    print(response1)
    print(response2)

    assert response1.data != response2.data

def test_index_template(client):
    response = client.get('/')
    assert b"Current Time in Moscow:" in response.data
    assert response.status_code == 200

    assert b"<title>Moscow Time</title>" in response.data
    assert b'<h1>Current Time in Moscow:</h1>' in response.data
