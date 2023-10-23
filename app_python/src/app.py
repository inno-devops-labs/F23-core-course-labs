"""
This module provides a simple web-server written in Flask.
The website displays current time.
"""

from datetime import datetime

import pytz
from flask import Flask
from prometheus_client import Summary

app = Flask(__name__)

CITY = {"text": "Moscow", "exact": "Europe/Moscow"}

# Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')


@REQUEST_TIME.time()
@app.route("/")
def index() -> str:
    """Return current time to an HTTP request."""
    city: str = CITY["text"]
    timezone = pytz.timezone(CITY["exact"])
    current_time: datetime = datetime.now(timezone)
    formatted_time: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return f"The current time in {city} is: {formatted_time}"


if __name__ == "__main__":
    # Flask server
    app.run(host="0.0.0.0", port=5000, threaded=True)
