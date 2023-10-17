from app_python.config import config
from datetime import datetime
from flask import request

def configure_routes(app):

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    # Displays current time in the timezone configured by the
    # TZ configuration variable according to the format from
    # the FORMAT configuration variable
    def display_time(path):

        ip: str = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
        
        now = datetime.now(tz=config["TZ"])
        
        time = now.strftime(config["FORMAT"])

        app.logger.info(f'Showing time {time} to {ip}')

        return time

