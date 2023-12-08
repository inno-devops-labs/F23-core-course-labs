"""Main module of web app"""
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from threading import Lock
import json
import os

COUNTER_PATH = '/data/counter.json'
counter_mutex = Lock()

if not os.path.isfile(COUNTER_PATH):
    with open(COUNTER_PATH, 'w+') as f:
        f.write(json.dumps({'count': 0}))

app = FastAPI()


@app.get("/")
async def root():
    "Response with current Moscow time"
    global counter_mutex

    with counter_mutex:
        with open(COUNTER_PATH, 'r') as f:
            data = json.load(f)
        data['count'] += 1
        with open(COUNTER_PATH, 'w') as f:
            f.write(json.dumps(data))

    return datetime.now(tz=ZoneInfo("Europe/Moscow")).strftime('%d/%m/%Y %H:%M')

@app.get("/visits")
async def visits():
    global counter_mutex

    with counter_mutex:
        with open(COUNTER_PATH, 'r') as f:
            data = json.load(f) 
        ret = str(data['count'])
        data['count'] += 1
        with open(COUNTER_PATH, 'w') as f:
            f.write(json.dumps(data))
        return f"Visits: {ret}"

@app.on_event('startup')
async def startup():
    Instrumentator().instrument(app).expose(app)