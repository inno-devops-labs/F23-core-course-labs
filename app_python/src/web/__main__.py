from aiohttp import web
import logging

from src.config import Config
from src.web.app import init_app


if __name__ == '__main__':
    config = Config()
    app = init_app()
    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app=app, host='0.0.0.0', port=config.PORT)
