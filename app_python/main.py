import logging
import os
from flask import Flask
from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)
logging.basicConfig(
    format='[%(levelname)-8s] %(asctime)-s:\t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)
path_to_volume = "./volume/visits.txt"

def update_visit_count():
    visit_count = 1
    if os.path.exists(path_to_volume):
        with open(path_to_volume, 'r') as file:
            visit_count = int(file.read()) + 1
    with open(path_to_volume, 'w') as file:
        file.write(str(visit_count))


def get_visit_count():
    if not os.path.exists(path_to_volume):
        return "0"
    with open(path_to_volume, 'r') as file:
        return file.read()


@app.route('/')
def current_time():
    # Get time in Moscow
    moscow_time = datetime.now(timezone(timedelta(hours=3)))
    logger.info(msg=f'Method: GET Response: {moscow_time}')
    update_visit_count()
    return f'Current time in Moscow: {moscow_time.strftime("%H:%M:%S")}'


@app.route('/visits')
def visits():
    return f'Number of visits: {get_visit_count()}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
