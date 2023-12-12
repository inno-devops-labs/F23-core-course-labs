from django.http import HttpResponse
from datetime import datetime
import pytz

visitsFileDir = "myproject/resources/visits"

def update_visits():
    try:
        with open(visitsFileDir, "r+") as f:
            val = int(f.read())
            f.seek(0)
            f.write(str(val + 1))
            f.truncate()
    except FileNotFoundError as e:
        with open(visitsFileDir, 'w+') as f:
 		        f.write("0")

def current_msk_time(request):
    # Updating visit number
    update_visits()

    #Set timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    #Get current time in Moscow
    moscow_time = datetime.now(moscow_tz)
    #Format time
    now = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f'Current time is: {now}')

def visits(
    request  # pylint: disable=unused-argument
):
    try:
        with open(visitsFileDir, "r") as f:
            return HttpResponse(f'{int(f.read())}')
    except FileNotFoundError as e:
        with open(visitsFileDir, 'w+') as f:
 		        f.write("0")
        return HttpResponse('0')
