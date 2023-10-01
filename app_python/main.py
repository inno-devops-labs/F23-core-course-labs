"""Main module of web app"""
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    "Response with current Moscow time"
    return datetime.now(tz=ZoneInfo("Europe/Moscow")).strftime('%d/%m/%Y %H:%M')
