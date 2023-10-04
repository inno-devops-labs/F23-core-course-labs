from app_python.config import config
from datetime import datetime

def configure_routes(app):

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    # Displays current time in the timezone configured by the
    # TZ configuration variable according to the format from
    # the FORMAT configuration variable
    def display_time(path):

        now = datetime.now(tz=config["TZ"])
        
        return now.strftime(config["FORMAT"])

