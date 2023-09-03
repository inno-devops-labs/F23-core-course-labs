from datetime import datetime
from zoneinfo import ZoneInfo

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route

def get_time(timezone: ZoneInfo = ZoneInfo("Europe/Moscow")) -> str:
    return datetime.now(timezone).strftime("%d/%m/%Y, %H:%M:%S")

async def homepage(request):
    response = f'Now in Moscow {get_time()}'
    return PlainTextResponse(response)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])