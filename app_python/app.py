from flask import Flask
from app_python.handlers.routes import configure_routes
from os import environ
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(module)s [%(levelname)s] : %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(host=environ.get("HOST", "0.0.0.0"))
