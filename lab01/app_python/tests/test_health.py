from main import app
from fastapi.testclient import TestClient


test_client = TestClient(app)


def test_health():
    resp = test_client.get('/health')
    assert resp.status_code == 200

