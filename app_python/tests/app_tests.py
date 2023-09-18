from datetime import datetime
from time import sleep
import unittest

from app import app, MSK_TIMEZONE


class TimeTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client()

    def test_get_time(self):
        self.__check_response__(self.tester)
        sleep(3)
        self.__check_response__(self.tester)

    def __check_response__(self, tester):
        response = tester.get('/', content_type='html/text')
        current_time_str = str(datetime.now(MSK_TIMEZONE).strftime('%H:%M:%S'))
        self.assertEqual(response.status_code, 200)
        # Check that time is correct
        response_data_str = response.data.decode("utf-8")
        self.assertTrue(current_time_str in response_data_str)


if __name__ == '__main__':
    unittest.main()
