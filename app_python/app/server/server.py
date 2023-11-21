"""
This module provides basic async http server.
"""

from aiohttp import web
from timeutils import timeutils
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Histogram
from prometheus_async.aio import time as prom_time


REQUEST_TIME = Histogram("request_processing_seconds",
                         "Time spent processing request")


@prom_time(REQUEST_TIME)
async def time_handler(request):
    print("got time request")
    return web.Response(text=timeutils.get_time())


async def metrics_handler(request):
    print(CONTENT_TYPE_LATEST)
    return web.Response(body=generate_latest(),
                        content_type="text/plain", charset="utf-8")


async def run_server(host: str, port: int):
    app = web.Application()
    app.add_routes(
        [web.get('/time', time_handler),
         web.get('/metrics', metrics_handler)
         ])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=host, port=port)
    await site.start()
    print(f"Server started at http://{host}:{port}")
