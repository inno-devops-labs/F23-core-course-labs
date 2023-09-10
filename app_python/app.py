from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route("/")
def moscow_time():
    # Get the current UTC time
    utc_time = datetime.now(timezone.utc)

    # Calculate the time difference for MSK (UTC+3)
    msk_time = utc_time + timedelta(hours=3)

    # Format the time as a string
    msk_time_str = msk_time.strftime("%Y-%m-%d %H:%M:%S")

    return f"Current Time in MSK: {msk_time_str}"
