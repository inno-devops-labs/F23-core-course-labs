from datetime import datetime
import logging
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import pytz
from waitress import serve

logging.basicConfig(
    format='%(levelname)-8s -- %(asctime)-s -- Message: \t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)


# Функция, которая возвращает время в определенном месте (в формате %H:%M:%S)
def get_timezone(name):
    return datetime.now(pytz.timezone(name)).strftime('%H:%M:%S')


# Создаем Flask app
app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
@metrics.counter('index_counter', 'Counter of index page visits')
def main():
    with open('./volume/visits', 'r') as file:
        visits = int(file.read()) + 1

    with open('./volume/visits', 'w') as file:
        file.write(str(visits))

    current_time = get_timezone('Europe/Moscow')
    logger.info(msg='Route: /')
    return render_template('index.html', current_time=current_time)


@app.route("/healthz")
def health_check():
    return app.response_class(
        response="OK",
        status=200,
        mimetype="text/plain"
    )


@app.route("/visits")
def get_visits():
    with open('./volume/visits', 'r') as file:
        visits = file.read()

    return app.response_class(
        response=str(visits),
        status=200,
        mimetype="text/plain"
    )


if __name__ == '__main__':
    serve(app, port=8080)
