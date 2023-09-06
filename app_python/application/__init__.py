from application.views.time import blue
from flask import Flask, render_template

def app():
    app = Flask(__name__)

    app.register_blueprint(blue)

    return app