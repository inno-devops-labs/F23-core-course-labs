import sys
from gunicorn.app.wsgiapp import run
from prometheus_client import start_http_server

if __name__ == '__main__':
    # Prometheus client
    start_http_server(8010)
    # Flask app
    sys.exit(run())
