from timeutils import timeutils


def test_timeutils_get_time():
    from zoneinfo import ZoneInfo
    import datetime

    time = datetime.datetime.now(tz=ZoneInfo(
        "Europe/Moscow")).strftime("%H:%M:%S")
    assert timeutils.get_time() == "Current time in Moscow: " + time
