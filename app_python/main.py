from datetime import datetime
from pytz import timezone
from flask import Flask
from threading import Lock

MOSCOW_TIMEZONE = timezone('Europe/Moscow')
FLASK_APP = Flask(__name__)

VISITS_FILENAME = '/assets/visits'
VISITS_LOCK = Lock()


def get_moscow_realtime():
    return datetime.now(MOSCOW_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")


@FLASK_APP.before_request
def middleware():
    with VISITS_LOCK:
        try:
            with open(VISITS_FILENAME, 'r') as f:
                VISITS = int(f.readline())
        except:
            VISITS = 0

        with open(VISITS_FILENAME, 'w') as f:
            f.write(str(VISITS + 1))


@FLASK_APP.route('/')
def index():
    return get_moscow_realtime()

@FLASK_APP.route('/visits')
def visits():
    with VISITS_LOCK:
        with open(VISITS_FILENAME) as f:
            VISITS = f.readline() 
        return str(VISITS)


# for testing
def return_flask_app_copy():
    return FLASK_APP


if __name__ == '__main__':
    FLASK_APP.run(host='0.0.0.0')
