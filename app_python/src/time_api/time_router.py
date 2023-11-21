import asyncio

from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from pytz import timezone
from datetime import datetime

time_api_router = APIRouter(
    prefix="/time",
    tags=["time"],
    responses={404: {"description": "Not found"}},
)

counter_lock = asyncio.Lock()
visits_file_path = "visits"


async def add_visit():
    async with counter_lock:
        try:
            with open(visits_file_path, "r") as f:
                visits = f.readline().strip()
                if visits is None or visits == "":
                    visits = 1
                else:
                    visits = int(visits) + 1
        except IOError:
            visits = 1
        with open(visits_file_path, "w") as f:
            f.writelines(str(visits))


@time_api_router.get("/moscow_time")
async def get_moscow_time() -> HTMLResponse:
    await add_visit()
    moscow_tz = timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    html_body = "<h1>Current Moscow Time</h1>"
    html_body += f"<p>Current date: {current_time.date()}</p>"
    html_body += f"<p>Current time: {current_time.time()}</p>"
    return HTMLResponse(content=html_body, status_code=200)
