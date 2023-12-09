import pytest
from .app import get_test_client
from bs4 import BeautifulSoup
import datetime
import pytz
from .config import timezone


@pytest.fixture
def test_client():

	return get_test_client()


def test_request(test_client):

	response = test_client.get('/')

	assert response.status_code == 200

	moscow_tz = pytz.timezone(zone=timezone)

	soup = BeautifulSoup(response.text, 'html.parser')
	response_time = soup.find('p').text
	response_time = datetime.datetime.strptime(response_time, '%H:%M:%S')
	response_time = moscow_tz.localize(response_time)

	current_time = datetime.datetime.now(moscow_tz)

	assert response_time - current_time < datetime.timedelta(seconds=5)
