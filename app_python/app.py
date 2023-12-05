from flask import Flask
from datetime import datetime, timezone, timedelta
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route("/")
def moscow_time():
    # Get the current UTC time
    utc_time = datetime.now(timezone.utc)

    # Calculate the time difference for MSK (UTC+3)
    msk_time = utc_time + timedelta(hours=3)

    # Format the time as a string
    msk_time_str = msk_time.strftime("%Y-%m-%d %H:%M:%S")

    return f"Current Time in MSK: {msk_time_str}"


if __name__ == "main":
    app.run(debug=True, host="0.0.0.0", port=5000)
