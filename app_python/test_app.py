from app import app
import time

def test_home_page_refresh():
    client = app.test_client()
    response1 = client.get('/')
    time.sleep(1) # wait for 1 second
    response2 = client.get('/')
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response2.data != response1.data # check if the response has changed