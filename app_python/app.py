from flask import Flask
import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/time', methods=["GET"])
def display_moscow_time():
    return get_moscow_time()

def get_moscow_time():
    # Get the current time in UTC
    utc_time = datetime.datetime.utcnow()
    moscow_offset = datetime.timedelta(hours=3) # Moscow is UTC+3 
    # Add the Moscow time offset to the UTC time
    moscow_time = utc_time + moscow_offset
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')

application = app

if __name__ == '__main__':
    application.run(host="0.0.0.0", port=5000)
