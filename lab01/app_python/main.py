from datetime import datetime

from fastapi import FastAPI
from pytz import timezone

app = FastAPI()


@app.get("/")
async def root():
    dt_format = "%d-%m-%Y %H:%M:%S"
    moscow_zone = datetime.now(timezone("Europe/Moscow"))
    return moscow_zone.strftime(dt_format)
