"""This module initializes the Flask application"""

from flask import Flask
from app.views.time_view import time_blueprint

def create_app():
    """The function creates an instance of flask app, registers blueprints and returns the app"""

    app = Flask(__name__)

    app.register_blueprint(time_blueprint)

    return app
