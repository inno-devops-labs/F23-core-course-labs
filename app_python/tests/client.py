import pytest
from httpx import AsyncClient
from app_python.src.main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
