"""
This module provides basic async http server.
"""
__author__ = "Artem Bulgakov"

from aiohttp import web
from timeutils import timeutils
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import Histogram
from prometheus_async.aio import time as prom_time
from threading import Lock
import json


class Visits:
    visits_file_lock: Lock = Lock()
    file_path = "/appdata/visits.txt"

    def __init__(self, file_path=None):
        self.file_path = file_path or self.file_path
        self._init_visits_file()

    def _init_visits_file(self) -> int:
        visits = 0
        with self.visits_file_lock:
            try:
                visits = self._read_visits_file()
            except (FileNotFoundError, ValueError):
                # If the file doesn't exist, create it and write '0'
                with open(self.file_path, 'w') as f:
                    f.write(str(visits))
        return visits

    def _read_visits_file(self) -> int:
        with open(self.file_path, 'r') as f:
            visits = int(f.read().strip())
            return visits

    def _write_visits_file(self, new_val) -> int:
        with open(self.file_path, 'w') as f:
            f.write(str(new_val))

    def increment_visits(self) -> None:
        with self.visits_file_lock:
            visits = self._read_visits_file()
            self._write_visits_file(visits+1)

    def get_visits(self) -> int:
        with self.visits_file_lock:
            return self._read_visits_file()


visits: Visits = None


REQUEST_TIME = Histogram("request_processing_seconds",
                         "Time spent processing request")


@prom_time(REQUEST_TIME)
async def time_handler(request):
    print("got time request")
    visits.increment_visits()
    return web.Response(text=timeutils.get_time(),
                        content_type="text/plain", charset="utf-8")


async def metrics_handler(request):
    print(CONTENT_TYPE_LATEST)
    return web.Response(body=generate_latest(),
                        content_type="text/plain", charset="utf-8")


async def visits_handler(request):
    visits_num = visits.get_visits()
    response_dict = {"visits": visits_num}
    response_json = json.dumps(response_dict)
    return web.Response(body=response_json,
                        content_type="application/json", charset="utf-8")


async def run_server(host: str, port: int):
    global visits
    visits = Visits()
    app = web.Application()
    app.add_routes(
        [web.get('/time', time_handler),
         web.get('/metrics', metrics_handler),
         web.get('/visits', visits_handler),
         ])
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host=host, port=port)
    await site.start()
    print(f"Server started at http://{host}:{port}")
