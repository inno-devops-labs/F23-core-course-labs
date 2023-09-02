"""Main module of web app"""
import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    "Response with current Moscow time"
    return datetime.datetime.now(tz=ZoneInfo("Europe/Moscow")).strftime('%d/%m/%Y %H:%M')
