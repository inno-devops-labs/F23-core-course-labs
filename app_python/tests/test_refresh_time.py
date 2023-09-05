import pytest
from src.app import app
import time


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_time_updates_on_refresh(client):
    response = client.get("/")
    initial_time = extract_time_from_response(response)
    time.sleep(2)
    response = client.get("/")
    refreshed_time = extract_time_from_response(response)
    assert initial_time != refreshed_time


def extract_time_from_response(response):
    return response.get_data(as_text=True).strip()
