import unittest
from app import get_moscow_time
from unittest.mock import patch
import datetime

class MockDateTime(datetime.datetime):
    @classmethod
    def utcnow(cls):
        # Fixed UTC time for testing
        return cls(2023, 1, 1, 12, 0, 0)

class TestMoscowTimeApp(unittest.TestCase):

    @patch('app.datetime.datetime', MockDateTime)
    def test_get_moscow_time(self):
        # Expected Moscow time (UTC+3)
        expected_moscow_time = '2023-01-01 15:00:00'

        # Call the function
        moscow_time = get_moscow_time()

        # Check if the returned time is as expected
        self.assertEqual(moscow_time, expected_moscow_time)

if __name__ == '__main__':
    unittest.main()