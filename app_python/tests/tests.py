from app import app

import unittest


class TimeTestCase(unittest.TestCase):
    def test_get_time(self):
        tester = app.test_client()
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()