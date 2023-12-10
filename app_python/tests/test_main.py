from fastapi.testclient import TestClient
from app_python.src.main import app
import time

client = TestClient(app)

def test_time_update():
    resp1 = client.get("/").json()
    time.sleep(2)
    resp2 = client.get("/").json()
    timestamp1 = resp1.split()[7]
    timestamp2 = resp2.split()[7]
    assert timestamp2 > timestamp1

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert 'Hello, User!' in response.json()