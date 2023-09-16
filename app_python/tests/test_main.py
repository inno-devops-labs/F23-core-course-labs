from starlette.testclient import TestClient

from src.main import app

client = TestClient(app=app)


def test_get_time():
    response = client.get("/")
    assert response.status_code == 200, "Expected 200 status"
    assert "time" in response.json(), 'Expected "time" word in response'


def test_get_updated_time():
    response1 = client.get("/")
    assert response1.status_code == 200, "Expected 200 status"

    response2 = client.get("/")
    assert response2.status_code == 200, "Expected 200 status"

    assert (
        response1.json()["time"] != response2.json()["time"]
    ), "Expected different date for different requests"
