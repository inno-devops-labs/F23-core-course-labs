from datetime import datetime, timedelta

moscow_utc_offset = 3
datetime_format = '%d-%m-%Y %H:%M:%S'

def get_moscow_time():
    moscow_datetime = datetime.utcnow() + timedelta(hours=moscow_utc_offset)
    (date, time) = moscow_datetime.strftime(datetime_format).split(' ')
    return (date, time)
