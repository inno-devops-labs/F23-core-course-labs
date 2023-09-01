from fastapi.testclient import TestClient
from datetime import datetime
from pytz import timezone

from .main import app

client = TestClient(app)


def test_get_current_moscow_timen():
    response = client.get("/")
    true_time = datetime.now(timezone('Europe/Moscow')).strftime("%H:%M:%S")

    assert response.status_code == 200
    assert response.json() == true_time
    