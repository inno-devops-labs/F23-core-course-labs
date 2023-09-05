import pytest
from src.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert b"Current Time in Moscow:" in response.data
    assert b"Date:" in response.data
    assert b"Time:" in response.data
