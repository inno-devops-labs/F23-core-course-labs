from datetime import datetime
import pytz

def get_date(timezone : str, format : str) -> str:
    tz = pytz.timezone(timezone)
    time_str = datetime.now(tz).strftime(format)
    return time_str