from flask import Flask
from config import DevelopmentConfig
import click
from flask.cli import with_appcontext
import pytest
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware


def create_app():
    app = Flask(__name__)
    app.wsgi_app = DispatcherMiddleware(
        app.wsgi_app, {"/metrics": make_wsgi_app()}
    )  # noqa: E501

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
