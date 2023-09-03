from main import app

from datetime import datetime, timedelta
from fastapi.testclient import TestClient
from pytz import timezone


tz = timezone("Europe/Moscow")
client = TestClient(app)


def test_moscow_time():
    response = client.get("/")
    assert response.status_code == 200

    client_time = datetime.fromisoformat(response.text)
    real_time = datetime.now(tz)
    assert real_time.utcoffset() == client_time.utcoffset()

    delta = real_time - client_time
    assert delta < timedelta(seconds=3)
