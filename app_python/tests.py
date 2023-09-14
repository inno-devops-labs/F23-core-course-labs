'''This module contains tests for the app.py module'''
from datetime import datetime
import unittest

from pytz import timezone
from app import app

class TestApp(unittest.TestCase):
    '''Class for testing app.py module'''

    def setUp(self):
        '''Set up client for testing'''
        self.app = app.test_client()
        self.app.testing = True


    def test_time_page(self):
        '''Send GET request to server'''
        response = self.app.get('/')

        moscow_time = datetime.now(
            timezone('Europe/Moscow')).strftime('%Y-%m-%d %H:%M:%S')

        #checks if the response is 200 and if the response contains the current time in Moscow
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            f'{moscow_time}', response.data.decode())


if __name__ == '__main__':
    unittest.main()
