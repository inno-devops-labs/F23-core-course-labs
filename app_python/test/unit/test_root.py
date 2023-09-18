from test.unit import client
from datetime import datetime, timezone, timedelta


def test_health(client):
    response = client.get("/")
    assert response.status_code == 200


def test_time(client):
    response = client.get("/")

    utc_time = datetime.now(timezone.utc)
    msk_time = utc_time + timedelta(hours=3)
    msk_time_str = msk_time.strftime("%Y-%m-%d %H:%M:%S")

    assert b"Current Time in MSK" in response.data
    assert bytes(msk_time_str, "utf-8") in response.data
