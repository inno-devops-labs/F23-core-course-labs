from flask import Flask
from api.route.time import time_blueprint
from flasgger import Swagger


def init() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(time_blueprint, url_prefix='/time')
    return app


app = init()

swagger = Swagger(app)
