from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root() -> datetime:
    """
    Get the current time in the 'Europe/Moscow' timezone.

    :return: A string representing the current time.
    :rtype: str
    """
    now = datetime.now(tz=ZoneInfo('Europe/Moscow'))
    return now
