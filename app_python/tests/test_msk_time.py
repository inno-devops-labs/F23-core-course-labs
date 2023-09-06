from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_get_moscow_time():
    response = client.get("/moscow-time")
    assert response.status_code == 200
    assert "time" in response.json()
