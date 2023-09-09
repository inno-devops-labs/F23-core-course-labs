import datetime

import pytest


@pytest.mark.asyncio
async def test_get_time(client_session) -> None:
    response = client_session.get("/")

    assert response is not None
    data = response.text

    assert data is not None

    data_start = "Current time in Moscow: "
    assert data.startswith(data_start)

    time = data.split(data_start)[1]
    assert datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S") is not None
