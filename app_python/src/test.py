import unittest
from app import app
import datetime
import pytz


class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_display_time_difference(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        # get time from page
        time_str = response.get_data(as_text=True).split(' ')[2]
        date_now = datetime.datetime.now().date()
        app_time = datetime.datetime.strptime(
            time_str, '%H:%M:%S'
        ).replace(year=date_now.year, month=date_now.month, day=date_now.day)
        app_time = pytz.timezone('Europe/Moscow').localize(app_time)

        # get actual current time
        actual_time = datetime.datetime.now(pytz.timezone('Europe/Moscow'))

        # check if time from page is correct
        diff = app_time - actual_time
        self.assertLessEqual(
            abs(diff.total_seconds()), 1
        )


if __name__ == '__main__':
    unittest.main()