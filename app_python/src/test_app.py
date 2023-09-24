from freezegun import freeze_time
from datetime import datetime
from bs4 import BeautifulSoup

from fastapi.testclient import TestClient
from httpx import Response

from src.app import app, format_time

client = TestClient(app)


def _test_common(time: datetime):
    with freeze_time(time):
        response: Response = client.get('/time')
        assert response.status_code == 200, 'Something went wrong in server'

        parsed = BeautifulSoup(response.content.decode(), 'html.parser')

        assert parsed.head.title.text == 'Current time'

        returned_text = parsed.find('div', {'class': 'time-block'}).text
        expected_text = f'Current time in Moskow is {format_time(time)}'
        assert returned_text == expected_text


def test_day():
    _test_common(datetime(2024, 3, 13))
    _test_common(datetime(2021, 5, 21))
    _test_common(datetime(2004, 7, 5))
    _test_common(datetime(1923, 1, 31))


def test_time():
    _test_common(datetime(2024, 3, 13, 3, 4, 5))
    _test_common(datetime(2021, 5, 21, 23, 59, 59))
    _test_common(datetime(2004, 7, 5, 0, 0, 0))
    _test_common(datetime(1923, 1, 31, 12, 30, 30))
