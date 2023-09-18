from fastapi.testclient import TestClient
from app_python.app import app
import time

client = TestClient(app)


def test_display_msk_time():
    response1 = client.get("/")
    assert response1.status_code == 200
    response1_time = response1.json()["Current time in Moscow is"]

    time.sleep(2)

    response2 = client.get("/")
    assert response2.status_code == 200
    response2_time = response2.json()["Current time in Moscow is"]

    assert response1_time != response2_time
