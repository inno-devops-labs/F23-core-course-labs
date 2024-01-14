from flask import Flask, Response
from datetime import datetime
from prometheus_client import generate_latest, Counter
import pytz

app = Flask(__name__)

healthcheck_counter = Counter(
    'healthcheck_requests',
    'Number of healthcheck requests'
)


@app.route('/healthcheck')
def healthcheck():
    healthcheck_counter.inc()  # Increment the healthcheck counter
    return 'Ok'


# Define a route for metrics
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


# Define a route to display the current time in Moscow
@app.route('/')
def display_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    return f'Current time in Moscow: {formatted_time}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
