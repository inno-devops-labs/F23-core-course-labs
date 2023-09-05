import requests
import re
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_main():
    response = requests.get('http://127.0.0.1:8000/')
    assert response.status_code == 200
    assert 'current time in moscow' in response.text.lower()
    assert len(re.findall(r'\d\d:\d\d:\d\d', response.text)) > 0