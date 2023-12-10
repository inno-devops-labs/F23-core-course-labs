from flask import Flask
import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/time', methods=["GET"])
def display_moscow_time():
    with open('./volume/visits', 'r') as f:
        visits = int(f.read()) + 1
    with open('./volume/visits', 'w') as f:
        f.write(str(visits))
    return get_moscow_time()

@app.route('/visits')
def visits():
    """
    Returns the rendered visits page template
    """
    with open('./volume/visits', 'r') as f:
        visits = f.read()

    return app.response_class(
        response=str(visits),
        status=200,
        mimetype="text/plain"
    )

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
