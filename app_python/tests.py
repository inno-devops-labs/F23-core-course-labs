import datetime
import unittest
import pytz
from app import app
from bs4 import BeautifulSoup


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_time(self):
        response = self.app.get('/?nocache=true')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        time_element = soup.find('p', id='moscow-time')

        time_str = time_element.get_text().strip()
        time_format = '%H:%M:%S'
        response_time = pytz.timezone('Europe/Moscow').localize(datetime.datetime.strptime(time_str, time_format))
        current_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))

        response_hms = (response_time.hour, response_time.minute, response_time.second)
        current_hms = (current_time.hour, current_time.minute, current_time.second)

        self.assertEqual(response_hms, current_hms)
