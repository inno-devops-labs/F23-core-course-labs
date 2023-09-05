import pytest
from datetime import datetime

from flaskr import create_app
from flaskr import util_functions as uf

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup will go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_datetime(client):
    response = client.get("/")
    datetime_now = uf.get_date("Europe/Moscow", '%Y-%m-%d %H:%M:%S')
    assert uf.compare_dates(datetime_now, response.data)
    
