"""Main module of web app"""
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
async def root():
    "Response with current Moscow time"
    return datetime.now(tz=ZoneInfo("Europe/Moscow")).strftime('%d/%m/%Y %H:%M')

@app.on_event('startup')
async def startup():
    Instrumentator().instrument(app).expose(app)