import datetime
from zoneinfo import ZoneInfo

import pytest


@pytest.mark.asyncio
async def test_get_page(client_session):
    """
    Test that the server returns a 200 status code for the homepage.
    """
    response = client_session.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_page_content_not_empty(client_session) -> None:
    response = client_session.get("/")
    assert response.text


@pytest.mark.asyncio
async def test_page_contains_time(client_session):
    """
    Test that the homepage contains the expected time information.
    """
    response = client_session.get("/")
    data = response.text

    prefix = "Current time in Moscow:"
    assert data.startswith(prefix)

    time_str = data.split(prefix)[1].strip()
    time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    assert time is not None


@pytest.mark.asyncio
async def test_time_is_correct(client_session):
    """
    Test that the time on the homepage is correct with a ±1 second variation.
    """
    response = client_session.get("/")
    data = response.text

    prefix = "Current time in Moscow:"
    time_str = data.split(prefix)[1].strip()

    test_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    test_time = test_time.replace(tzinfo=ZoneInfo("Europe/Moscow"))
    current_time = datetime.datetime.now(ZoneInfo("Europe/Moscow"))

    assert abs(current_time - test_time) < datetime.timedelta(seconds=1)
