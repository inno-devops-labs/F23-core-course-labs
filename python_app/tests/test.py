import unittest
from time import sleep

from app import app
from app import get_current_time


class TimeZonedTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_time_is_correct(self):
        response = self.app.get('/?nocache=true')
        self.assertEqual(response.status_code, 200)  # check if the website is working

        data = response.get_data(as_text=True)
        app_time = data[data.index('<h1>')+4:data.index('</h1>')]  # subtract the time displayed on the website

        current_time = get_current_time()

        self.assertEqual(app_time, current_time)

    def test_time_updates_on_refresh(self):
        first_response = self.app.get('/')
        sleep(2)
        second_response = self.app.get('/')

        initial_data = first_response.get_data(as_text=True)
        current_data = second_response.get_data(as_text=True)

        self.assertNotEquals(initial_data, current_data)
