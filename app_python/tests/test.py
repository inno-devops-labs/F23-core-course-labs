import unittest
from fastapi.testclient import TestClient
from src.main import app
import time

client = TestClient(app)

class AppTest(unittest.TestCase):
    def test_response(self):
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
    
    def test_diff(self):
        res1 = client.get("/")
        time.sleep(1)
        res2 = client.get("/")
        self.assertNotEqual(res1.json(), res2.json())

    def test_erorr(self):
        response = client.get("/blabla")

        self.assertEqual(response.status_code, 404)