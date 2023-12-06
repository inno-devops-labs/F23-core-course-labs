"""
This module provides a simple web-server written in Flask.
The website displays current time.
"""

from datetime import datetime
import os

import pytz
from flask import Flask
from prometheus_client import Summary

app = Flask(__name__)

CITY = {"text": "Moscow", "exact": "Europe/Moscow"}

# Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


visits_file = "data/visits"

def get_visits_count():
    if not os.path.exists(visits_file):
        with open(visits_file, "w") as f:
            f.write("0")
        return 0
    else:
        with open(visits_file) as f:
            return int(f.read())

def increment_visits_count():
    count = get_visits_count()
    count += 1
    with open(visits_file, "w") as f:
        f.write(str(count))


@REQUEST_TIME.time()
@app.route("/")
def index() -> str:
    """Return current time to an HTTP request."""
    increment_visits_count()

    city: str = CITY["text"]
    timezone = pytz.timezone(CITY["exact"])
    current_time: datetime = datetime.now(timezone)
    formatted_time: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return f"The current time in {city} is: {formatted_time}"


@app.route("/visits")
def visit():
    count = get_visits_count()
    return f"{count}"


if __name__ == "__main__":
    # Flask server
    app.run(host="0.0.0.0", port=5000, threaded=True)
