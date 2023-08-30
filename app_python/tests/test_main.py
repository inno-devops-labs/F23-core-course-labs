import pytest


@pytest.mark.anyio
async def test_get_time(async_app_client):
    response = await async_app_client.get("/")
    assert response.status_code == 200
    assert "time" in response.json()


@pytest.mark.anyio
async def test_invalid_path(async_app_client):
    response = await async_app_client.get("/invalid")
    assert response.status_code == 404
