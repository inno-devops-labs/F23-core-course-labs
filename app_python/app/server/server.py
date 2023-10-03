"""
This module provides basic async http server.
"""
__author__ = "Artem Bulgakov"

from aiohttp import web
from timeutils import timeutils


async def time_handler(request):
    return web.Response(text=timeutils.get_time())


async def run_server(host: str, port: int):
    app = web.Application()
    app.add_routes(
        [web.get('/time', time_handler)
         ])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=host, port=port)
    await site.start()
    print(f"Server started at http://{host}:{port}")
