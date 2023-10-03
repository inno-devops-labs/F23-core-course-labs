import pytz
from datetime import datetime


class TimeProvider:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_current_datetime(tz=pytz.timezone('Europe/Moscow')) -> datetime:
        return datetime.now(tz)
