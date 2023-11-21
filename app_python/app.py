"""
Main file for Moscow Time application
"""

from datetime import datetime
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics
import pytz

app = Flask(__name__)
metrics = PrometheusMetrics(app)

COUNTER_FILE = 'visit_counter.txt'

def read_counter():
    """Reads the counter value from the file."""
    if os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'r') as file:
            return int(file.read())
    return 0

def update_counter():
    """Increments the counter and saves it to the file."""
    count = read_counter() + 1
    with open(COUNTER_FILE, 'w') as file:
        file.write(str(count))
    return count

@app.route('/')
def index():
    """Route gets time and returns template page with time variable"""
    moscow_time = get_time()
    return render_template('index.html', time=moscow_time)

@app.route('/time')
def get_time():
    """Route provides Moscow time"""
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    return moscow_time

@app.route('/visits')
def visits():
    """Route to display the number of visits."""
    count = read_counter()
    return count

if __name__ == '__main__':
    app.run()
