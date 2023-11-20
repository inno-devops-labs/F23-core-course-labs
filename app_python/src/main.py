"""
Entrypoint for application
"""
from datetime import datetime
from zoneinfo import ZoneInfo
from threading import Lock
import os.path
import json

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette_exporter import PrometheusMiddleware, handle_metrics

from starlette.middleware.base import BaseHTTPMiddleware

COUNTER_FILE = '/data/counter.json'

counterLock = Lock()
if not os.path.isfile(COUNTER_FILE):
    with open(COUNTER_FILE, 'w+') as f:
        f.write(json.dumps({'counter': 0}))

class CounterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # pylint: disable=unused-argument
        global counterLock
        response_task = call_next(request)

        # Well, it's not a best solution I can do, but it's the simpliest one
        with counterLock:
            with open(COUNTER_FILE, 'r') as f:
                data = json.load(f)

            data['counter'] += 1

            with open(COUNTER_FILE, 'w') as f:
                f.write(json.dumps(data))

        return await response_task


def get_time(timezone: ZoneInfo = ZoneInfo("Europe/Moscow")) -> str:
    """Fetch current time and convert to desired timezone"""
    return datetime.now(timezone).strftime("%d/%m/%Y, %H:%M:%S")

async def homepage(request):
    # pylint: disable=unused-argument
    """Handler for root entrypoint"""
    response = f'Now in Moscow {get_time()}'
    return PlainTextResponse(response)

async def visited(request):
    global counterLock
    """Handler for visited endpoint"""
    with counterLock:
        with open(COUNTER_FILE, 'r') as f:
            data = json.load(f)
            return PlainTextResponse(str(data['counter']))


app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage),
        Route('/metrics', handle_metrics),
        Route('/visited', visited),
    ],
    middleware=[
        Middleware(CounterMiddleware),
        Middleware(
            PrometheusMiddleware,
            app_name='python_app'
        )
    ]
)
