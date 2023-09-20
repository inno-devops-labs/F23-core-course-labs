import unittest
from app import app, get_moscow_time

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_display_moscow_time_endpoint(self):
        response = self.app.get('/time')
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.data.decode('utf-8'), r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

    def test_get_moscow_time(self):
        moscow_time = get_moscow_time()
        self.assertRegex(moscow_time, r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')

if __name__ == '__main__':
    unittest.main()
