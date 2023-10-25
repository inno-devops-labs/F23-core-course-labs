from app_python.config import config
from datetime import datetime
from flask import request, Response

from prometheus_client import Summary, generate_latest

def configure_routes(app):
    request_duration = Summary('http_request_duration_seconds', 'HTTP request duration in seconds')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    @request_duration.time()
    # Displays current time in the timezone configured by the
    # TZ configuration variable according to the format from
    # the FORMAT configuration variable
    def display_time(path):

        ip: str = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
        
        now = datetime.now(tz=config["TZ"])
        
        time = now.strftime(config["FORMAT"])

        app.logger.info(f'Showing time {time} to {ip}')

        return time
    
    @app.route('/metrics')
    def metrics():
        CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


