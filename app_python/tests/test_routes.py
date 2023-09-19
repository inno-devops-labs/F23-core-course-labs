import datetime
import time
import sys
import os
import pytest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from application.app import create_app  # noqa: E402


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


"""
Test for checking if the page returns the moscow time with code 200
"""


def test_get_moscow_time(client):
    response = client.get("/")
    assert response.status_code == 200

    date = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(date)
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    assert formatted_time.encode() in response.data


"""
Test for checking if the moscow time is updating and not hardcoded
"""


def test_check_moscow_time_changes(client):
    response1 = client.get("/")
    assert response1.status_code == 200

    date = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time1 = datetime.datetime.now(date)
    formatted_time1 = moscow_time1.strftime("%Y-%m-%d %H:%M:%S")

    assert formatted_time1.encode() in response1.data

    time.sleep(1)

    response2 = client.get("/")
    assert response2.status_code == 200

    moscow_time2 = datetime.datetime.now(date)
    formatted_time2 = moscow_time2.strftime("%Y-%m-%d %H:%M:%S")

    assert formatted_time2.encode() in response2.data
    assert formatted_time1 != formatted_time2
