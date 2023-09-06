import pytest
import time

from app_python.app import app


@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


def check_time_format(message):
    prefix = 'Current Moscow time is '
    if not message.startswith(prefix):
        return False
    message = message[len(prefix):]
    try:
        time.strptime(message, '%Y-%m-%d, %H:%M:%S.%f')
        return True
    except ValueError:
        return False


def check_response(response):
    return response.status_code == 200


# Testing return time format
def test_moscow_time(client):
    response = client.get("/")
    assert check_response(response)

    _time = response.data.decode('utf-8')
    assert check_time_format(_time)


# Testing that after refresh time changed
def test_time_changed(client):
    time1 = client.get("/").data.decode('utf-8')
    time.sleep(1)
    time2 = client.get("/").data.decode('utf-8')
    assert time1 != time2
