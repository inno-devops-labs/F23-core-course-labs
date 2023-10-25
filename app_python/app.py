from flask import Flask, render_template
import datetime
import pytz
from prometheus_flask_exporter import PrometheusMetrics
import prometheus_client

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.3')


@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    # Set the current time as a metric
    return render_template('time.html', time=formatted_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
