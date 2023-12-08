from fastapi.testclient import TestClient
from app_python.src.main import app
from datetime import datetime
from time import sleep
import pytz

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == datetime.now(pytz.timezone('Europe/Moscow')).\
        ctime()


def test_update_main():
    response1 = client.get("/")
    sleep(1)
    response2 = client.get("/")
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() < response2.json()
