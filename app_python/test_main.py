import time

from fastapi.testclient import TestClient

from main import app

test_client = TestClient(app)


def test_time_changes():
    response_a = test_client.get('/')
    time.sleep(1)
    response_b = test_client.get('/')
    # if responses are not equal the time has changed
    assert response_a.content != response_b.content


def test_200_response():
    response = test_client.get('/')
    assert response.status_code == 200


def test_404_response():
    response = test_client.get('/non-existing-path')
    assert response.status_code == 404
