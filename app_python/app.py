import argparse
from datetime import datetime, timezone, timedelta
import logging
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
from waitress import serve

logging.basicConfig(
    format='[%(levelname)-8s] %(asctime)-s:\t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)

MSK_TIMEZONE = timezone(timedelta(hours=3))

app = Flask(__name__)
metrics = PrometheusMetrics(app)

parser = argparse.ArgumentParser()

parser.add_argument("-prod", "--production", action='store_true')


@app.route('/')
@metrics.counter('index_page_counter', 'Index page counter')
def show_time():
    # Get current time in Moscow timezone
    time_now = datetime.now(MSK_TIMEZONE).strftime('%H:%M:%S')
    logger.info(msg=f'Method: GET Response: {time_now}')
    return render_template('index.html', current_time=time_now)


if __name__ == '__main__':
    is_prod = parser.parse_args().production

    if is_prod:
        serve(app, port=8000)
    else:
        app.run()
