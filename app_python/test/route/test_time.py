def test_request_time(client):
    response = client.get("time/")
    assert response.json["time"]
    assert response.json["timezone"] == 'Europe/Moscow'
    assert response.status_code == 200


def test_two_request(client):
    response_1 = client.get("time/")
    response_2 = client.get("time/")

    assert response_2.json["timezone"] == response_1.json["timezone"]
    assert response_1.json["timezone"] == 'Europe/Moscow'
    assert response_1.json["time"] <= response_2.json["time"]
