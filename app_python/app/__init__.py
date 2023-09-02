from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.views.time_view import time_blueprint
    app.register_blueprint(time_blueprint)

    return app