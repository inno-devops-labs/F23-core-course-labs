import pytz
from datetime import datetime


def current_formatted_time(timezone='Europe/Moscow') -> str:
    timezone_object = pytz.timezone(timezone)
    return datetime.now(timezone_object).strftime('%Y-%m-%d %H:%M:%S %Z%z')
