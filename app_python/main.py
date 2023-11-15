from flask import Flask
from datetime import datetime
import pytz
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def moscow_time():
    timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(timezone)
    formatted_time = time.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
    return 'Current Moscow time is ' + formatted_time

if __name__ == '__main__':
    serve(app=app, port="5000")