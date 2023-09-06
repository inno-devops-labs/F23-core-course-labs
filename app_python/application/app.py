from flask import Flask
from config import DevelopmentConfig
import click
from flask.cli import with_appcontext
import pytest


def create_app():
    app = Flask(__name__)

    from . import routes

    app.register_blueprint(routes.bp)

    app.config.from_object(DevelopmentConfig)
    app.template_folder = app.config["TEMPLATES_FOLDER"]
    app.static_folder = app.config["STATIC_FOLDER"]

    @click.command()
    @with_appcontext
    def test():
        pytest.main(["-v", "-s", "tests"])

    app.cli.add_command(test)

    return app
