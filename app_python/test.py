import time
import unittest
from flask import Flask
from main import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index(self):
        response1 = self.app.get("/")
        time.sleep(1)
        response2 = self.app.get("/")

        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertIn(b"Moscow", response1.data)
        self.assertIn(b"Moscow", response2.data)
        self.assertNotEqual(response1.data, response2.data)


if __name__ == "__main__":
    unittest.main()
