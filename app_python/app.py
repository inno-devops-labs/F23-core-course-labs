"""
The main application
"""
from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)


@app.route('/')
def home():
    """
    Returns the rendered home page template
    """
    with open('./volume/visits', 'r') as f:
        visits = int(f.read()) + 1
    with open('./volume/visits', 'w') as f:
        f.write(str(visits))
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
