from datetime import datetime
from time import sleep
import pytz

from src.time_provider import TimeProvider


def test_get_current_time():
    assert TimeProvider.get_current_datetime().strftime('%H:%M:%S') == datetime.now(
        tz=pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
    sleep(3)
    assert TimeProvider.get_current_datetime().strftime('%H:%M:%S') == datetime.now(
        tz=pytz.timezone('Europe/Moscow')).strftime('%H:%M:%S')
