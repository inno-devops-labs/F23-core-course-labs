from datetime import datetime

import pytz


def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    return datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
