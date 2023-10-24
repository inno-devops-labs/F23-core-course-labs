from flask import Flask, jsonify
from api.route.time import time_blueprint
from flasgger import Swagger
from prometheus_client import start_http_server, Counter

def init() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(time_blueprint, url_prefix='/time')
    return app

app = init()

swagger = Swagger(app)


@app.route('/metrics')
def metrics():
    from prometheus_client.exposition import generate_latest
    return generate_latest()

request_counter = Counter('myapp_requests_total', 'Total number of requests to /')

# Function to increment the request counter
def increment_request_counter():
    request_counter.inc()

# Define a sample route
@app.route('/')
def hello():
    increment_request_counter()  # Increment the request counter
    return jsonify(message="Hello, World!")
