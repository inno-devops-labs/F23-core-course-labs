from flask import Flask, Response
from datetime import datetime
from prometheus_client import generate_latest, Counter
import pytz

app = Flask(__name__)

healthcheck_counter = Counter(
    'healthcheck_requests',
    'Number of healthcheck requests'
)

visit_counter = Counter(
    'route_visits',
    'Number of visits to the "/" route'
)


@app.route('/healthcheck')
def healthcheck():
    healthcheck_counter.inc()  # Increment the healthcheck counter
    return 'Ok'


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), content_type='text/plain')


@app.route('/')
def display_time():
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    formatted_time = moscow_time.strftime('%Y-%m-%d %H:%M:%S')
    visit_counter.inc()
    return f'Current time in Moscow: {formatted_time}'


@app.route('/visits')
def display_visits():
    visit_count = int(visit_counter._value.get())
    with open('volume/visits', 'w') as visits_file:
        visits_file.write(str(visit_count))
    return f'Number of visits to "/": {visit_count}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8008)
