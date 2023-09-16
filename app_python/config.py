from os import environ
import pytz

config = {
    'TZ': pytz.timezone(environ.get("CLOCK_TZ", "Europe/Moscow")),
    'HOST': environ.get("HOST", "0.0.0.0"),
    'FORMAT': "%Y-%m-%d %H:%M:%S"
} 