from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo
import os


def create_app(visits_file_path='data/visits', reset=False):
    visits_file_path = os.path.expanduser(visits_file_path)

    app = Flask(__name__)

    if not os.path.isfile(visits_file_path):
        os.makedirs(os.path.dirname(visits_file_path), exist_ok=True)
        with open(visits_file_path, 'w' if reset else 'a') as _:
            pass

    @app.route('/')
    def time_in_moscow():
        moscow_timezone = ZoneInfo('Europe/Moscow')
        ret = datetime.now(tz=moscow_timezone).time().__str__()
        with open(visits_file_path, 'a') as visits_file:
            visits_file.write(ret + '\n')
        return ret

    @app.route('/visits')
    def visits_history():
        with open(visits_file_path) as visits_file:
            return visits_file.read()

    return app