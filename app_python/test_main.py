import datetime
from unittest.mock import MagicMock
from fastapi.testclient import TestClient

from .main import app
from .schemas.time import NowTime

client = TestClient(app)

def test_time_now(monkeypatch):
    '''Tests that /api/time/now returns correct date for each request'''

    # Mocking datetime.datetime
    datetime_mock = MagicMock(wrap=datetime.datetime)
    monkeypatch.setattr('app_python.routers.time.datetime', datetime_mock)

    # Set mock value for utcnow
    mocked_time = datetime.datetime(2020, 3, 11, 0, 0, 0)
    correct_time = mocked_time + datetime.timedelta(hours=3)
    datetime_mock.utcnow.return_value = mocked_time

    # Ensure response format, status and correctness
    response = client.get("/api/time/now")
    assert response.status_code == 200
    assert NowTime(**response.json()) == NowTime(timestamp=correct_time)

    # Ensure that response is always actual
    mocked_time = datetime.datetime(2020, 3, 12, 0, 0, 0)
    correct_time = mocked_time + datetime.timedelta(hours=3)
    datetime_mock.utcnow.return_value = mocked_time

    response = client.get("/api/time/now")
    assert response.status_code == 200
    assert NowTime(**response.json()) == NowTime(timestamp=correct_time)

def test_index():
    '''Tests that / returns same page as /index.html'''

    # Ensure response status
    index_response = client.get("/")
    assert index_response.status_code == 200

    # Ensure response status
    index_html_response = client.get("/index.html")
    assert index_html_response.status_code == 200

    assert index_response.text == index_html_response.text
