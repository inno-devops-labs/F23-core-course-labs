
def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    expected = "The current time in Moscow is: "
    assert expected in res.get_data(as_text=True)
