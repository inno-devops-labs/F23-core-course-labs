import datetime
import unittest
from time import sleep
from src.app import app

FIND_STRING = "Moscow Time: "
TIME_STRING_LENGTH = len("HH:MM:SS")


def extract_time_from_response(response):
    """
    :param response: TestResponse
    :return: time object extracted from response
    """
    body = response.text
    find_string_index = body.index(FIND_STRING)
    time_string_index_start = find_string_index + len(FIND_STRING)
    time_string_index_end = time_string_index_start + TIME_STRING_LENGTH
    time_string = body[time_string_index_start:time_string_index_end]

    return datetime.datetime.strptime(time_string, "%H:%M:%S")


class TimeServerTests(unittest.TestCase):
    def test_page_available(self):
        """
        Check page availability and it's content besides time
        """

        response = app.test_client().get("/")

        self.assertEqual(response.status_code, 200)

    def test_page_text_correct(self):
        """
        Check text "Moscow Time: " is in the response body text
        """

        response = app.test_client().get("/")
        self.assertIn("Moscow Time: ", response.text)

    def test_time_increase_on_refresh(self):
        """
        Check time displayed on the page increases on each page refresh
        """

        response1 = app.test_client().get("/")
        sleep(1)
        response2 = app.test_client().get("/")

        time1 = extract_time_from_response(response1)
        time2 = extract_time_from_response(response2)

        print(time1, time2)
        self.assertGreater(time2, time1)


if __name__ == "__main__":
    unittest.main()
