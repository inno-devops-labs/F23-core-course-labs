from datetime import datetime
import pytz

def get_date(timezone : str, format : str) -> str:
    tz = pytz.timezone(timezone)
    time_str = datetime.now(tz).strftime(format)
    return time_str


def str_to_datetime(dt : str) -> datetime:
    # handling some weirdness of response format.
    # e.g. there is an added hyphen at the end when converting to
    # bytes. Need to handle.
    if type(dt) is bytes:
        dt = str(dt)
        dt = dt[-20:-1]
    else:
        dt = dt[-19:]
    datetime_obj = datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')

    return datetime_obj


def datetime_to_minutes(dt : datetime) -> int:
    return (
        dt.year * 365 * 24 * 60 +
        dt.month * 30 * 24 * 60 +
        dt.day * 24 * 60 +
        dt.hour * 60 +
        dt.minute
    )


def compare_dates(datetime_a : str, datetime_b : str) -> bool:
    minutes_a = datetime_to_minutes(str_to_datetime(datetime_a))
    minutes_b = datetime_to_minutes(str_to_datetime(datetime_b))

    # Keep relatively high margin of error of 2 minutes to
    # prevent false-negatives from high ping.
    return abs(minutes_a - minutes_b) < 2
