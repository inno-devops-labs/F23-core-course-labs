import time
import unittest
from flask import Flask
from src import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_response(self):
        response = self.app.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Moscow", response.data)

    def test_response_update(self):
        response1 = self.app.get("/")
        time.sleep(1)
        response2 = self.app.get("/")

        self.assertNotEqual(response1.data, response2.data)


if __name__ == "__main__":
    unittest.main()
