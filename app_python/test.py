"""Test functions for web app"""
import datetime
from zoneinfo import ZoneInfo
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """Test get request on root /"""
    now = datetime.datetime.now(tz=ZoneInfo("Europe/Moscow"))
    now_formatted = now.strftime('"%d/%m/%Y %H:%M"')
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == now_formatted
