from fastapi import FastAPI
from datetime import datetime
import zoneinfo
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get("/")
async def root():
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    return {"time": datetime.now(zone)}
