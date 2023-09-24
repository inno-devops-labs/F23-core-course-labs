from app import app


def test_home_route():
    client = app.test_client()

    response = client.get('/')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response data contains the expected content
    assert b'Current time in Moscow:' in response.data
