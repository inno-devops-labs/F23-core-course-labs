from flask import Flask
from datetime import datetime
import pytz
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics


# Creating a Flask package
app = Flask(__name__)
metrics = PrometheusMetrics(app)


# Defining a route to show Moscow time
@app.route('/')
def moscow_time():
    timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(timezone)
    formatted_time = time.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
    return 'Current Moscow time is ' + formatted_time


# Running the package
if __name__ == '__main__':
    serve(app=app, port="8080")
