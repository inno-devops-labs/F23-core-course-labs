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

    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'

    # @app.route('/post/test', methods=['POST'])
    # def receive_post():
    #     headers = request.headers

    #     auth_token = headers.get('authorization-sha256')
    #     if not auth_token:
    #         return 'Unauthorized', 401

    #     data_string = request.get_data()
    #     data = json.loads(data_string)

    #     request_id = data.get('request_id')
    #     payload = data.get('payload')

    #     if request_id and payload:
    #         return 'Ok', 200
    #     else:
    #         return 'Bad Request', 400
