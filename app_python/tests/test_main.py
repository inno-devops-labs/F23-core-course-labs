import pytest
import time
from datetime import datetime

from app_python.src.config import TIME_FORMAT
from app_python.tests.client import client


@pytest.mark.anyio
async def test_get_time(client):
    resp = await client.get("/")
    assert resp.status_code == 200, f"Incorrect status code: {resp.status_code}"

    body = resp.json()
    assert "current_time" in resp.json(), f"Incorrect body: {body}"

    t1 = datetime.strptime(body["current_time"], TIME_FORMAT)
    time.sleep(1)

    resp = await client.get("/")
    body = resp.json()
    assert "current_time" in resp.json(), f"Incorrect body for second request: {body}"

    t2 = datetime.strptime(body["current_time"], TIME_FORMAT)

    assert t1 < t2, "Time is constant and not updating"
