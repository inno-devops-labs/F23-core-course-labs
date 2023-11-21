"""
This module displays moscow time
"""
from datetime import datetime
import os

import pytz
from flask import Flask, render_template
# from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)

COUNTER = './visits.txt'

def get_current_visits():
    try:
        if os.path.exists(COUNTER):
            with open(COUNTER, 'r') as file:
                return int(file.read())
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return 0

def update_visits():
    try:
        current_visits = get_current_visits()
        if os.path.exists(COUNTER):
            with open(COUNTER, 'w') as file:
                file.write(str(current_visits + 1))
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")
    return 0

@app.route("/visits")
def visits():
    return str(get_current_visits())

@app.route("/")
def get_time():
    """
    Return moscow time as html
    """
    mtz = pytz.timezone("Europe/Moscow")
    time_in_moscow = datetime.now(mtz)
    time_formated = time_in_moscow.strftime("%H:%M:%S")
    update_visits()
    return render_template('time.html', time=time_formated)

@app.errorhandler(404)
def not_found():
    """
    Return error page not found as html
    """
    return render_template("error.html"),404

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
