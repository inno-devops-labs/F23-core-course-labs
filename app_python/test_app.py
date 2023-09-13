from app import app
from datetime import datetime
from pytz import timezone
import pytest
import time


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_refresh(client):
    response = client.get('/')
    assert response.status_code == 200
    moscow_time = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    assert moscow_time in str(response.data)


def test_curr_time_return(client):
    response = client.get('/')
    moscow_time = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    assert response.status_code == 200
    assert moscow_time in str(response.data)


def test_time_changes_on_refresh(client):
    response1 = client.get('/')
    moscow_time1 = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    time.sleep(1)
    response2 = client.get('/')
    moscow_time2 = datetime.now(timezone('Europe/Moscow')).strftime('%H:%M:%S')
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert moscow_time1 in str(response1.data)
    assert moscow_time2 in str(response2.data)
    assert moscow_time1 != moscow_time2
