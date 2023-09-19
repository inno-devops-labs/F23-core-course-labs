from datetime import datetime
from run import client


def test_format(client):
    landing = client.get("/")
    dt = str(landing.data).split("'")[1]
    assert datetime.strptime(dt, "%d/%m/%Y %H:%M:%S")


def test_status(client):
    landing = client.get("/")
    assert landing.status_code == 200


