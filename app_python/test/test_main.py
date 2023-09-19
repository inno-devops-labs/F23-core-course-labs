from datetime import datetime, timezone
import sys
import os
from zoneinfo import ZoneInfo

from freezegun import freeze_time

from main import get_time

@freeze_time(datetime.utcfromtimestamp(0))
def test_zero_date_gmt_zero():
    # Input/mocks and expected output
    expected = "01/01/1970, 00:00:00"

    # Execution
    actual = get_time(ZoneInfo('Etc/GMT+0'))
    assert expected == actual

@freeze_time(datetime.utcfromtimestamp(0))
def test_zero_date_moscow():
    # Input/mocks and expected output
    expected = "01/01/1970, 03:00:00"

    # Execution
    actual = get_time(ZoneInfo('Europe/Moscow'))
    assert expected == actual
