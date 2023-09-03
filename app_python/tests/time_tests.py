import unittest
from time import sleep

from app import app, get_timezone


class TimeTest(unittest.TestCase):
    def test_correctness_of_time(self):
        tester = app.test_client()
        response = tester.get('/', content_type='html/text').data.decode("utf-8")
        current_time = get_timezone('Europe/Moscow')
        self.assertTrue(current_time in response)

    def test_change_of_time(self):
        tester = app.test_client()
        response1 = tester.get('/', content_type='html/text').data.decode("utf-8")
        sleep(1)
        response2 = tester.get('/', content_type='html/text').data.decode("utf-8")
        self.assertTrue(response1 != response2)


if __name__ == '__main__':
    unittest.main()
