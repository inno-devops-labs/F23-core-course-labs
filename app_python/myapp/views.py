"""views module"""
from datetime import datetime, timezone, timedelta
from django.http import HttpResponse

visitsNumberFilePath = "myapp/resources/visits"

def current_time(
    request  # pylint: disable=unused-argument
):
    """returns current time"""
    moscow_tz = timezone(timedelta(hours=3))
    now = datetime.now(moscow_tz)
    try:
        with open(visitsNumberFilePath, "r+") as f:
            current_number = int(f.read())
            f.seek(0)
            f.write(str(current_number + 1))
            f.truncate()
    except FileNotFoundError as e:
        create_file(visitsNumberFilePath)
    return HttpResponse(now.strftime('%Y-%m-%d %H:%M:%S'))

def visits(
    request  # pylint: disable=unused-argument
):
    try:
        with open(visitsNumberFilePath, "r") as f:
            return int(f.read())
    except FileNotFoundError as e:
        create_file(visitsNumberFilePath)
        return 0


def create_file(filePath):
 	with open(filePath, 'w+') as f:
 		f.write("0")