"""This module initializes the Flask application"""

from flask import Flask
from app.views.time_view import time_blueprint
from app.views.metrics_view import metrics_blueprint

def create_app():
    """The function creates an instance of flask app, registers blueprints and returns the app"""

    app = Flask(__name__)

    app.register_blueprint(time_blueprint)
    app.register_blueprint(metrics_blueprint)
    return app
