"""views module"""
from datetime import datetime, timezone, timedelta
from django.http import HttpResponse


def current_time(
    request  # pylint: disable=unused-argument
):
    """returns current time"""
    moscow_tz = timezone(timedelta(hours=3))
    now = datetime.now(moscow_tz)
    return HttpResponse(now.strftime('%Y-%m-%d %H:%M:%S'))
