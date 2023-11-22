from flask import Flask
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics
import pytz
import os

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

def update_visits():
    try:
        current_visits = get_current_visits()
        if os.path.exists(path):
            with open(path, 'w') as file:
                file.write(str(current_visits + 1))
    except Exception as e:
        print(e)
    return 0

@app.route("/visits")
def visits():
    return str(get_current_visits())


@app.route('/')
# Get current time in Moscow
def current_time_moscow():
    update_visits()
    # Set timezone
    moscow_tz = pytz.timezone('Europe/Moscow')
    # Get current time in Moscow
    moscow_time = datetime.now(moscow_tz)
    # Format time
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    # Return time
    return f'Current time in Moscow: {formatted_time}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
