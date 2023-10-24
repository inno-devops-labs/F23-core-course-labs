from datetime import datetime

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pytz import timezone

app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    dt_format = "%d-%m-%Y %H:%M:%S"
    moscow_zone = datetime.now(timezone("Europe/Moscow"))
    return moscow_zone.strftime(dt_format)

@app.get("/health", status_code=200)
async def health():
    return "Server is healthy"