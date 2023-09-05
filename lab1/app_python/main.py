from datetime import datetime
from pytz import timezone
from flask import Flask

MOSCOW_TIMEZONE = timezone('Europe/Moscow')
FLASK_APP = Flask(__name__)


def get_moscow_realtime():
    return datetime.now(MOSCOW_TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")


@FLASK_APP.route('/')
def index():
    return get_moscow_realtime()


# for testing
def return_flask_app_copy():
    return FLASK_APP


if __name__ == '__main__':
    FLASK_APP.run()
