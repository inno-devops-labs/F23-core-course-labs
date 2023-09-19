import pytest

from app_python.run import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client
