import unittest
from app import app
import datetime
import pytz
from bs4 import BeautifulSoup


class TestDisplayTime(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_display_time_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_display_time_difference(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        # Use BeautifulSoup to parse the HTML response
        soup = BeautifulSoup(
            response.get_data(as_text=True),
            'html.parser'
        )

        # Find the <p> element containing the time
        time_paragraph = soup.find('p')

        # Extract the time string from the <p> element
        app_time_str = time_paragraph.text.strip()

        # Parse the time string into a datetime object (offset-aware)
        app_time = datetime.datetime.strptime(
            app_time_str, '%Y-%m-%d %H:%M:%S'
        )
        app_time = pytz.timezone('Europe/Moscow').localize(app_time)

        # Get the current time in Moscow (offset-aware)
        current_time_moscow = datetime.datetime.now(
            pytz.timezone('Europe/Moscow')
        )

        # Calculate the time difference
        time_difference = app_time - current_time_moscow
        print("\nThe absolute time difference is: " 
              + str(abs(time_difference)))
        self.assertLessEqual(
            abs(time_difference.total_seconds()), 5
        )


if __name__ == '__main__':
    unittest.main()
