from flask import Flask
from app_python.handlers.routes import configure_routes
from os import environ

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(host=environ.get("HOST", "0.0.0.0"))
