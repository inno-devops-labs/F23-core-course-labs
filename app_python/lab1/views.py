from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from zoneinfo import ZoneInfo


def index(request):
    return HttpResponse(str(datetime.now(tz=ZoneInfo("Europe/Moscow"))))