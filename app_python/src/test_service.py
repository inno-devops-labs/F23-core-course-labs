import datetime
import time
import unittest


class TimerTest(unittest.TestCase):
    def testTimer(self):
        from app_python.src import service

        timer = service.Timer()

        self.assertIsNotNone(timer)

        first = timer.now()
        time.sleep(0.01)
        second = timer.now()

        self.assertGreater(second - first, datetime.timedelta(seconds=0.01))

        self.assertEqual(str(first.utcoffset()), "3:00:00")
        self.assertEqual(str(second.utcoffset()), "3:00:00")
