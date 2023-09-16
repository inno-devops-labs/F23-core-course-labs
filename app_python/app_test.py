import time

import pytz, pytest
from datetime import  datetime
from index import app
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_current_time(client):
    response = client.get('/')
    assert response.status_code == 200
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    assert f"{current_time.strftime('%Y:%m:%d %H:%M:%S')}" in str(response.data)

def test_refresh(client):
    response1 = client.get('/')
    assert response1.status_code == 200
    time.sleep(2)
    response2 = client.get('/')
    assert response2.status_code == 200
    assert response2.data != response1.data