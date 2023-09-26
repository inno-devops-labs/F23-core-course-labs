import datetime
from application.app import create_app
import unittest


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_get_moscow_time(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

        date = datetime.timezone(datetime.timedelta(hours=3))
        moscow_time = datetime.datetime.now(date)
        formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

        self.assertIn(formatted_time.encode(), response.data)
