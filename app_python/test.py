from datetime import datetime
import unittest
import pytz
from app import app, get_current_time
from bs4 import BeautifulSoup
import unittest
import time


class TestWibSite(unittest.TestCase):
    """Class for testing my web application"""
    def setUp(self):
        """Function taht init data for testing"""
        self.app = app.test_client()

    def test_time_updates_on_refresh(self):
        response_1 = self.app.get("/")
        time.sleep(2)
        response_2 = self.app.get("/")

        content_1 = response_1.get_data(as_text=True)
        content_2 = response_2.get_data(as_text=True)

        self.assertNotEqual(content_1, content_2)


    def test_time(self):
        response = self.app.get('/?nocache=true')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.data, 'html.parser')
        time_str = soup.find('h1', id='moscow-time').get_text().strip()

        response_time = pytz.timezone('Europe/Moscow').localize(datetime.strptime(time_str, '%H:%M:%S'))
        current_time = datetime.now(pytz.timezone('Europe/Moscow'))

        response_hms = (response_time.hour, response_time.minute, response_time.second)
        current_hms = (current_time.hour, current_time.minute, current_time.second)

        self.assertEqual(response_hms, current_hms)


if __name__ == "__main__":
    unittest.main()