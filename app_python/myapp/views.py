from django.http import HttpResponse
from datetime import datetime, timezone, timedelta

def current_time(request):
    moscow_tz = timezone(timedelta(hours=3))
    now = datetime.now(moscow_tz)
    return HttpResponse(now.strftime('%Y-%m-%d %H:%M:%S'))


