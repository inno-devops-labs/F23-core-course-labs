import datetime
import pytz
import logging

from visits_counter import VisitsCounter


class Timer:
    """

    Timer is a class that provides simple interface to work with time

    """

    def __init__(self, counter: VisitsCounter, logger: logging.Logger):
        self.MoscowTimezone = pytz.timezone("Europe/Moscow")
        self.logger = logger
        self.counter = counter

    def now(self):
        now = datetime.datetime.now(tz=self.MoscowTimezone)
        self.logger.log(
            level=logging.INFO,
            msg=f"time was requested, returned: {now}",
        )
        self.counter.update()
        return datetime.datetime.now(tz=self.MoscowTimezone)
