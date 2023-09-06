from flask import request
import json
from app_python.config import config
from datetime import datetime

def configure_routes(app):
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def display_time(path):

        now = datetime.now(tz=config["TZ"])
        
        return now.strftime(config["FORMAT"])

