import datetime
import unittest

from app import flask_app
from logic import get_moscow_time


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_moscow_time_format(self):
        """Test the get_moscow_time function for returning
        Moscow time in the correct format."""
        time_format = "%Y-%m-%d %H:%M:%S"
        moscow_time = get_moscow_time()

        try:
            # Try to convert the returned time into a datetime object.
            # If it fails, it's not in the expected format.
            datetime.datetime.strptime(moscow_time, time_format)
        except ValueError:
            assert False, \
                "The returned Moscow time is not in the expected format."

    def test_moscow_time_endpoint(self):
        """Test the main endpoint for Moscow time."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current Moscow Time', response.data)

    def test_healthcheck_endpoint(self):
        """Test the healthcheck endpoint."""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'status', response.data)
        self.assertIn(b'healthy', response.data)


if __name__ == "__main__":
    unittest.main()
