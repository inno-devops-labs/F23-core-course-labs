"""This module contains functions testing application funcionalities"""
from datetime import datetime
import re
import pytest
from bs4 import BeautifulSoup
from app import create_app



@pytest.fixture
def client():
    """This function initializes flask applications"""
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as app_client:
        yield app_client


def test_date_time(client):
    """This functions tests that time returned by server matches the current time"""
    time_format = "%Y-%m-%d %H:%M:%S"

    before_time = datetime.now().replace(microsecond=0)

    response = client.get('/')

    after_time = datetime.now()

    assert response.status_code == 200, f"Expected ok but got status code = {response.status_code}"

    soup = BeautifulSoup(response.data, 'html.parser')


    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    result = pattern.search(str(soup))

    assert result is not None, "date and time not found"

    server_time = datetime.strptime(result.group(), time_format)

    assert before_time <= server_time <= after_time, \
        f"Expected to be in between {before_time} and {after_time} but got {server_time}"
