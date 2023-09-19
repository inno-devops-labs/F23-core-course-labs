
def test_request_time(client):
    response = client.get("time/")
    assert b'Europe/Moscow' in response.data
