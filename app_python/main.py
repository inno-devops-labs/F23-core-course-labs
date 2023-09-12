"""
This module provides a simple web-server written in Flask.
The website displays current time.
"""

from datetime import datetime
import pytz
from flask import Flask

app = Flask(__name__)

CITY = {"text": "Moscow", "exact": "Europe/Moscow"}


@app.route("/")
def index(    ) -> str:
    """Return current time to an HTTP request."""
    city: str = CITY["text"]
    timezone = pytz.timezone(CITY["exact"])
    current_time: datetime = datetime.now(timezone)
    formatted_time: str = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return f"The current time in {city} is: {formatted_time}"


if __name__ == "__main__":
    app.run()
