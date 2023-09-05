from aiohttp import web

from src.config import Config
from src.web.app import init_app


if __name__ == '__main__':
    config = Config()
    app = init_app()

    web.run_app(app=app, host='0.0.0.0', port=config.PORT)
