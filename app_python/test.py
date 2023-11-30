from datetime import datetime, timezone, timedelta
from flask.testing import FlaskClient
from main import return_flask_app_copy
import pytest


@pytest.fixture
def app():
    yield return_flask_app_copy()


@pytest.fixture
def client(app):
    return app.test_client()


def get_moscow_time_without_timezone():
    return (datetime
            .now(timezone.utc)
            .astimezone(timezone(timedelta(hours=3)))
            .strftime("%Y-%m-%d %H:%M:%S"))


def test_get_time(client: FlaskClient):
    response = client.get('/')

    assert response.status_code == 200
    assert response.data.decode() == get_moscow_time_without_timezone()

    # page refresh emulation
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == get_moscow_time_without_timezone()
