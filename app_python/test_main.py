import unittest
import socketserver
import requests
import datetime
import threading

from main import TimeServer


class TestTimeServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=cls.start_server)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    @classmethod
    def start_server(cls):
        server_address = ('localhost', 8008)
        cls.server = socketserver.TCPServer(server_address, TimeServer)
        print(cls.server.server_address)
        print(cls.server.address_family)
        cls.server.serve_forever()

    def test_time_server_conntection(self):
        try:
            response = requests.get('http://127.0.0.1:8008/')
        except requests.exceptions.ConnectionError:
            print("Connection is fault")
            raise

        self.assertEqual(response.status_code, 200)

    def test_time_servertime(self):
        try:
            before_time = datetime.datetime.utcnow()
            before_time += datetime.timedelta(hours=3)
            response = requests.get('http://localhost:8008/')

            after_time = datetime.datetime.utcnow()
            after_time += datetime.timedelta(hours=3)

            after_time_str = after_time.strftime('%Y-%m-%d %H:%M')
            before_time_str = before_time.strftime('%Y-%m-%d %H:%M')

            if (after_time_str != before_time_str):
                before_time = datetime.datetime.utcnow()
                before_time += datetime.timedelta(hours=3)
                response = requests.get('http://localhost:8008/')
                after_time = datetime.datetime.utcnow()
                after_time += datetime.timedelta(hours=3)

                after_time_str = after_time.strftime('%Y-%m-%d %H:%M')
                before_time_str = before_time.strftime('%Y-%m-%d %H:%M')

            substr = 'The current time in Moscow is '+after_time_str
            self.assertIn(substr, response.text)
        except KeyboardInterrupt:
            self.tearDown()


if __name__ == '__main__':
    unittest.main()
