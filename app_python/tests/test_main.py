import time

from starlette.testclient import TestClient

from src.main import app

client = TestClient(app=app)


def test_get_time():
    """Test that GET request returns 200 status"""
    acceptable_status = 200

    response = client.get("/")
    assert (
        response.status_code == acceptable_status
    ), f"Expected {acceptable_status} status"

    assert "time" in response.json(), 'Expected "time" word in response'


def test_updating_time():
    """Test that date in request increasing in timeline"""
    response1 = client.get("/")

    time.sleep(1)

    response2 = client.get("/")

    seconds1 = get_seconds_from_response(response1)
    seconds2 = get_seconds_from_response(response2)

    assert (
        seconds2 > seconds1
    ), "Expected seconds in seconds greater than second in first date"


def get_seconds_from_response(response):
    date = response.json()["time"]
    return int(date.split(":")[2].split(".")[0])
