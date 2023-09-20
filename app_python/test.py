from application import app
import unittest
import time


class TestApp(unittest.TestCase):

    # initialize
    def start(self):
        self.app = app.test_client()

    # test url link for work
    def if_url(self):
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, 200)

    # check if time updates on every response
    def if_updates(self):
        # send first try
        try_1 = self.app.get("/")
        # wait
        time.sleep(5)
        # send second try
        try_2 = self.app.get("/")
        
        result_1 = try_1.get_data(as_text=True)
        result_2 = try_2.get_data(as_text=True)

        # compare
        self.assertNotEqual(result_1, result_2)


if __name__ == "__main__":
    unittest.main()