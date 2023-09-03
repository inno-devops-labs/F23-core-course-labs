from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pytz import timezone


app = FastAPI()
tz = timezone("Europe/Moscow")


@app.get("/")
def root():
    return PlainTextResponse(datetime.now(tz).isoformat())
