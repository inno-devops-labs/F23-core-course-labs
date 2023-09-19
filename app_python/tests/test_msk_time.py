# tests/test_integration.py
import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_get_moscow_time():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/time")
        assert response.status_code == 200
        data = response.json()
        assert "time" in data

@pytest.mark.asyncio
async def test_invalid_timezone():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        response = await client.get("/time?timezone=InvalidTimezone")
        assert response.status_code == 400
        assert "detail" in response.json()
