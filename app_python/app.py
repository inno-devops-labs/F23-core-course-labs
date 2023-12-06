from flask import Flask
from datetime import datetime
import pytz
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics


# Creating a Flask package
app = Flask(__name__)
visits_path = "./volume/visits"
metrics = PrometheusMetrics(app)


# Function for reading visits
def read_visits():
    return int(open(visits_path, "r").read())


# Function for reading visits
def write_visits(visits):
    f = open(visits_path, "w")
    f.write(str(visits))
    f.close()


# Defining a route to show Moscow time
@app.route('/')
def moscow_time():
    write_visits(read_visits() + 1)

    timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(timezone)
    formatted_time = time.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
    return 'Current Moscow time is ' + formatted_time


# Defining a route to show visits count
@app.route("/visits")
def get_visits():
    return str(read_visits())


# Running the package
if __name__ == '__main__':
    serve(app=app, port="8080")
