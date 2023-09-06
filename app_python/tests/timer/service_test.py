import datetime
import time
import unittest

import pytz


class TimerTest(unittest.TestCase):
    def test_timer(self):
        from app_python.src.timer import service

        timer = service.Timer()

        self.assertIsNotNone(timer)

        first = timer.now()
        time.sleep(0.01)
        second = timer.now()

        self.assertGreater(second - first, datetime.timedelta(seconds=0.01))

        self.assertEqual(str(first.utcoffset()), "3:00:00")
        self.assertEqual(str(second.utcoffset()), "3:00:00")


if __name__ == '__main__':
    unittest.main()
