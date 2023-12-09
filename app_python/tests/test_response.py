"""
Tests moduel for for the time displayment
"""
from main import app


def test_response():
    """
    Test if the response is 200 for accessing home
    """
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200

def test_error():
    """
    Test if the response is 404 for accessing route doesn't exist
    """
    with app.test_client() as test_client:
        response = test_client.get("/error")
        assert response.status_code != 200

def test_time():
    """
    Test if the response has time within
    """
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert b"time" in response.data
