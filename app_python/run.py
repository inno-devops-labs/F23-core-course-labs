from datetime import datetime
import pytz
from flask import Flask


TIMEZONE = 'Europe/Moscow'
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"


app = Flask(__name__)


def update_number():
    f = open('visits/visits.txt', 'r+', encoding="utf-8")
    lines = f.readlines()
    if len(lines) > 0:
        num = int(lines[0]) + 1
    else:
        num = 1

    f.seek(0)
    f.truncate()
    f.write(str(num))
    f.close()

    return str(num)


@app.route('/')
def get_moscow_time():
    update_number()

    moscow_time = datetime.now(pytz.timezone(TIMEZONE))
    formatted_time = moscow_time.strftime(DATETIME_FORMAT)
    return formatted_time


@app.route('/visits')
def get_visits():
    return update_number()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
