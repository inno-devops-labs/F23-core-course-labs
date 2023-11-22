''' Flask application that displays current time in GMT+3 timezone.'''

import datetime
import pytz
import os
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

path = '/data/visits.txt'

def get_current_visits():
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                return int(file.read())
    except Exception as e:
        print(e)
    return 0

@app.route("/visits")
def visits():
    return str(get_current_visits())

def update_visits():
    try:
        current_visits = get_current_visits()
        if os.path.exists(path):
            with open(path, 'w') as file:
                file.write(str(current_visits + 1))
    except Exception as e:
        print(e)
    return 0

@app.route('/')
def index():
    update_visits()
    """Get current time in GMT+3 timezone."""
    moscow = pytz.timezone('Europe/Moscow')
    # Format time to YYYY-MM-DD HH:MM:SS
    time = datetime.datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
