import time

import pytz
import pytest
from datetime import datetime
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_current_time(client):
    response = client.get('/')
    assert response.status_code == 200
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    formatted_time = f"{current_time.strftime('%H:%M:%S')}"
    assert formatted_time in str(response.data)


def test_refresh(client):
    response1 = client.get('/')
    assert response1.status_code == 200
    time.sleep(2)
    response2 = client.get('/')
    assert response2.status_code == 200
    assert response2.data != response1.data


def test_wrong_url(client):
    response = client.get('/test')
    assert response.status_code == 404
