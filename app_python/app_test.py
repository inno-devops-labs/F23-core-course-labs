from falcon import testing
from app import create
from datetime import datetime, timezone, timedelta


class TestCase(testing.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        self.app = create()


TIME_FORMAT = '%a %d %b %Y, %I:%M:%S %p'


class Test(TestCase):
    def test_get_moscow_time(self):
        res = self.simulate_get('/')
        res_datetime = datetime.strptime(res.text, TIME_FORMAT)

        tz = timezone(timedelta(hours=3))
        current_datetime = datetime.strptime(datetime.now(tz)
                                             .strftime(TIME_FORMAT), TIME_FORMAT)
        self.assertLessEqual(
            abs(current_datetime.timestamp() - res_datetime.timestamp()),
            2)
