import os
import sys

dir_name = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(dir_name, "..")
sys.path.insert(0, project_dir)

from pytz import timezone
from src.timezone import get_moscow_time
from datetime import datetime

datetime_format = '%d-%m-%Y %H:%M:%S'

def test_get_moscow_time():
    moscow_timezone = timezone("Europe/Moscow")
    (expected_date, expected_time) = datetime.now(moscow_timezone).strftime(datetime_format).split(' ')
    (actual_date, actual_time) = get_moscow_time()
    assert expected_date == actual_date
    assert expected_time == actual_time
