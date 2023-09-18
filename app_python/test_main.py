import unittest
import socketserver
import requests
import datetime
import threading

from main import TimeServer


class TestTimeServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.serverthread = threading.Thread(target=cls.startserver)
        cls.serverthread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.serverthread.join()

    @classmethod
    def startserver(cls):
        serveraddress = ('localhost', 8008)
        cls.server = socketserver.TCPServer(serveraddress, TimeServer)
        print(cls.server.server_address)
        print(cls.server.address_family)
        cls.server.serve_forever()

    def testtimeserverconntection(self):
        try:
            response = requests.get('http://127.0.0.1:8008/')
        except requests.exceptions.ConnectionError:
            print("Connection is fault")
            raise

        self.assertEqual(response.status_code, 200)

    def testtimeservertime(self):
        try:
            beforetime = datetime.datetime.utcnow()
            beforetime += datetime.timedelta(hours=3)
            response = requests.get('http://localhost:8008/')

            aftertime = datetime.datetime.utcnow()
            aftertime += datetime.timedelta(hours=3)

            aftertimestr = aftertime.strftime('%Y-%m-%d %H:%M')
            beforetimestr = beforetime.strftime('%Y-%m-%d %H:%M')

            if (aftertimestr != beforetimestr):
                beforetime = datetime.datetime.utcnow()
                beforetime += datetime.timedelta(hours=3)
                response = requests.get('http://localhost:8008/')
                aftertime = datetime.datetime.utcnow()
                aftertime += datetime.timedelta(hours=3)

                aftertimestr = aftertime.strftime('%Y-%m-%d %H:%M')
                beforetimestr = beforetime.strftime('%Y-%m-%d %H:%M')

            substr = 'The current time in Moscow is '+aftertimestr
            self.assertIn(substr, response.text)
        except KeyboardInterrupt:
            self.tearDown()


if __name__ == '__main__':
    unittest.main()
