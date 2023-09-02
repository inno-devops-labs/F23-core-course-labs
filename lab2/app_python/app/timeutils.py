"""
This module provides utility functions for time.
"""
__author__ = "Artem Bulgakov"


def get_time() -> str:
    import datetime
    from zoneinfo import ZoneInfo
    dt = datetime.datetime.now(
        tz=ZoneInfo("Europe/Moscow")
        )
    time = dt.strftime("%H:%M:%S")
    return "Current time in Moscow: " + time
