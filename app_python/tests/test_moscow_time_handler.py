import pytest

from datetime import datetime, timedelta

from src.web.app import init_app


@pytest.mark.asyncio
async def test_time_refresh(aiohttp_client) -> None:
    # arrange
    app = await init_app()
    web_client = await aiohttp_client(app)

    # act
    response1 = await web_client.get('/')
    response2 = await web_client.get('/')

    # assert
    assert response1.status == 200
    assert response2.status == 200

    time_recv1 = datetime.fromisoformat(await response1.text())
    time_recv2 = datetime.fromisoformat(await response2.text())
    delta = time_recv2 - time_recv1

    assert (delta > timedelta(0)) and delta < timedelta(minutes=1)
