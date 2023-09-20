"""
Test cases for Web app.
"""

import unittest
from time import sleep

from app import app
from app import get_current_time


class TimeZonedTimeTestCase(unittest.TestCase):
    """
    Test case class for Web app.
    """

    def setUp(self):
        """
        Set up the testing client.
        """
        self.app = app.test_client()

    def test_time_is_correct(self):
        """
        Test the correctness of the time displayed.
        """

        response = self.app.get('/?nocache=true')
        self.assertEqual(response.status_code, 200)  # check if the website is working

        data = response.get_data(as_text=True)
        app_time = data[data.index('<h1>') + 4:data.index('</h1>')]  # subtract the displayed time

        current_time = get_current_time()

        self.assertEqual(app_time, current_time)

    def test_time_updates_on_refresh(self):
        """
        Test that refreshing the page updates the time.
        """

        first_response = self.app.get('/')
        sleep(2)
        second_response = self.app.get('/')

        initial_data = first_response.get_data(as_text=True)
        current_data = second_response.get_data(as_text=True)

        self.assertNotEqual(initial_data, current_data)
