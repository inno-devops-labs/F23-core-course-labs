''' Flask application that displays current time in GMT+3 timezone.'''

import datetime
import pytz
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def index():
    """Get current time in GMT+3 timezone."""
    moscow = pytz.timezone('Europe/Moscow')
    # Format time to YYYY-MM-DD HH:MM:SS
    time = datetime.datetime.now(moscow).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
