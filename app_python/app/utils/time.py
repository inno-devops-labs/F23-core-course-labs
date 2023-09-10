"""This module contains helpful functions to time"""

from datetime import datetime
import pytz


def moscow_timezone():
    """returns moscow timezone"""
    return pytz.timezone("Europe/Moscow")

def moscow_time():
    """returns moscow time"""

    current_moscow_time = datetime.now(moscow_timezone())

    return current_moscow_time
