"""
This module contains unit tests for the Flask web application.
"""

from datetime import datetime
import unittest
from app import app, MOSCOW_TZ

class TestTimeDisplay(unittest.TestCase):
    """
    Test class for the time display functionality of the web application.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        """
        test = app.test_client()
        self.test_display_time(test)

    def test_display_time(self, test):
        """
        Test the display_time function.

        Sends a GET request to the app's root URL, retrieves the response,
        and checks if it contains the current Moscow time.

        Args:
            test: The Flask test client.
        """
        # Send a GET request to the app's root URL
        response = test.get('/', content_type='html/text')

        moscow_time_str = str(datetime.now(MOSCOW_TZ).strftime('%Y-%m-%d %H:%M:%S'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if time is true
        response_data_str = response.data.decode("utf-8")
        self.assertTrue(moscow_time_str in response_data_str)

if __name__ == '__main__':
    unittest.main()
