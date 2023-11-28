from flask import Flask, jsonify
from api.route.time import time_blueprint
from flasgger import Swagger
from prometheus_client import start_http_server, Counter
import os


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


request_counter = Counter('myapp_requests_total',
                          'Total number of requests to /')

# Function to increment the request counter


def increment_request_counter():
    request_counter.inc()

# Define a sample route

filename = './visits'

@app.route('/')
def hello():
    increment_request_counter()  # Increment the request counter
    increment()
    return jsonify(message="Hello, World!")


@app.route('/visits')
def visits():
    with open(filename, 'r') as f:
        s = f.read()
        res = 0
        if s != '':
            res = int(s)
        return res


def increment():
    s = ''
    create_file_if_not_exists(filename)
    with open(filename, 'r') as f:
        s = f.read()
    res = 0
    if s != '':
        res = int(s)
    with open(filename, 'w') as f:
        f.write(str(res + 1))


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")


def create_file_if_not_exists(file_path):
    directory = os.path.dirname(file_path)
    create_directory_if_not_exists(directory)

    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            print(f"File '{file_path}' created.")
    else:
        print(f"File '{file_path}' already exists.")
