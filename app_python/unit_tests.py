from datetime import datetime
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)


@pytest.mark.parametrize("path", ["/"])
def test_get_response_status_code(path):
    response = client.get(path)
    assert response.status_code == 200


@pytest.mark.parametrize("path", ["/"])
def test_get_response_content(path):
    response = client.get(path)
    assert "currentTime" in response.text


@pytest.mark.parametrize("path", ["/"])
def test_get_current_time_format(path):
    response = client.get(path)
    html_content = response.text
    current_time_start = html_content.find(
        "<div class='time'>") + len("<div class='time'>")
    current_time_end = html_content.find("</div>")

    current_time = html_content[current_time_start:current_time_end].strip()

    try:
        datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        pytest.fail("Formatted time is not in the expected format")
