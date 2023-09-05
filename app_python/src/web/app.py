from aiohttp import web
from typing import List

from src.domain.time_tracker import MOSCOW_TIMEZONE_SHIFT, UTCTimeTracker
from src.web.handlers import TimeWebHandler, WebHandler


async def __init_handlers() -> List[WebHandler]:
    web_handlers = []
    web_handlers.append(TimeWebHandler(UTCTimeTracker, MOSCOW_TIMEZONE_SHIFT))

    return web_handlers


async def _init_routers(app: web.Application, handlers: List[WebHandler]) -> None:
    for handler in handlers:
        app.router.add_routes(handler.get_routers())


async def init_app() -> web.Application:
    app = web.Application()
    handlers = await __init_handlers()
    await _init_routers(app, handlers)

    return app
