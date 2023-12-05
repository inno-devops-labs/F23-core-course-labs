"""
Web App main logic.
"""
from datetime import datetime
from threading import Lock
import os.path
import json

import pytz
from flask import Flask, render_template

import config

app = Flask(__name__)
visits_data_file_path = 'data/visits.json'
visits_data_lock = Lock()

if not os.path.exists(visits_data_file_path):
    os.mkdir('data')
    os.mknod(visits_data_file_path)

with open(visits_data_file_path, 'w+') as file:
    file.write(json.dumps({'counter': 0}))


@app.route('/')
def index():
    """
    Get rendered HTML template with filled data.
    """
    current_time = get_current_time()

    with visits_data_lock:
        with open(visits_data_file_path, 'r') as file:
            data = json.load(file)

        data['counter'] += 1

        with open(visits_data_file_path, 'w') as file:
            file.write(json.dumps(data))

    return render_template('index.html', current_time=current_time)


@app.route("/visits")
def visits():
    try:
        with open(visits_data_file_path, 'r') as file:
            counter = json.load(file)['counter']
    except FileNotFoundError:
        counter = 0

    return render_template('visits.html', visits=counter)


def get_current_time():
    """ Getting formatted time in Moscow time-zone """

    moscow_timezone = pytz.timezone(config.TIME_ZONE)
    time = datetime.now(moscow_timezone)

    return time.strftime(config.TIME_FORMAT)


if __name__ == '__main__':
    app.run()
