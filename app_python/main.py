"""
Entrypoint for application
"""
from datetime import datetime
from zoneinfo import ZoneInfo

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

def get_time(timezone: ZoneInfo = ZoneInfo("Europe/Moscow")) -> str:
    """Fetch current time and convert to desired timezone"""
    return datetime.now(timezone).strftime("%d/%m/%Y, %H:%M:%S")

async def homepage():
    """Handler for root entrypoint"""
    response = f'Now in Moscow {get_time()}'
    return PlainTextResponse(response)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
