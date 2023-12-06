"""
This is a FastAPI application that returns
the current date and time in the "Europe/Moscow" timezone.
"""

from zoneinfo import ZoneInfo
from datetime import datetime
from fastapi import FastAPI, status, Response
from prometheus_fastapi_instrumentator import Instrumentator
import json
import os
from threading import Lock

COUNT_FILE = '/data/counter.json'
mutex = Lock()

if not os.path.isfile(COUNT_FILE):
    with open(COUNT_FILE, 'w+') as f:
        f.write(json.dumps({'count': 0}))

app = FastAPI()
@app.get("/")
async def read_main():
    """
    Get the current date and time in the "Europe/Moscow" timezone and return it as a message.

    Returns:
        str: A greeting message along with the current date and time.
    """
    global mutex

    with mutex:
        with open(COUNT_FILE, 'r') as f:
            data = json.load(f)
        data['count'] += 1
        with open(COUNT_FILE, 'w') as f:
            f.write(json.dumps(data))

    current_time = datetime.now(tz=ZoneInfo(
                    "Europe/Moscow")).strftime("%d/%m/%Y %H:%M:%S")
    return f"Hello, User! The date and time: {current_time}"

@app.get("/healthch")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)

@app.get("/visits")
async def visits():
    global mutex

    with mutex:
        with open(COUNT_FILE, 'r') as f:
            data = json.load(f) 
        ret = str(data['count'])
        data['count'] += 1
        with open(COUNT_FILE, 'w') as f:
            f.write(json.dumps(data))
        return f"Number of visits: {ret}"

@app.on_event('startup')
async def startup():
    Instrumentator().instrument(app).expose(app)
