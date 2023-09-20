import datetime
import pytz


class Timer:
    """

    Timer is a class that provides simple interface to work with time

    """

    def __init__(self):
        self.MoscowTimezone = pytz.timezone("Europe/Moscow")

    def now(self):
        return datetime.datetime.now(tz=self.MoscowTimezone)
