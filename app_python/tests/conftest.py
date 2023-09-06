from fastapi.testclient import TestClient
import pytest

from lab1.app_python.app import app


@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    return client
