from datetime import datetime
from zoneinfo import ZoneInfo

from django.http import HttpResponse


def index(request):
    return HttpResponse("time: " + str(datetime.now(tz=ZoneInfo("Europe/Moscow"))))


def visits(request):
    with open("visit-counter.txt", "r+") as file:
        try:
            visits_count = int(file.readline().strip())
        except Exception:
            visits_count = 0
        visits_count += 1
        file.seek(0)
        file.write(str(visits_count))
        file.truncate()
        return HttpResponse(str(visits_count))
