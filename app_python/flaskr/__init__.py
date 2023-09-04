import os

from flask import Flask

#from app_python.flaskr.get_date import get_date

def create_app(test_config = None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app = Flask(__name__)

    @app.route('/')
    def home():
        # this import goes against PEP 8 but this is how it's done in flask according to docs
        from . import util_functions as uf

        return "Time in Moscow: " + uf.get_date("Europe/Moscow", '%Y-%m-%d %H:%M:%S')

    if __name__ == '__main__':
        app.run()

    return app