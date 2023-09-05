from fastapi import FastAPI
from datetime import datetime
import zoneinfo

app = FastAPI()


@app.get("/")
async def root():
    zone = zoneinfo.ZoneInfo("Europe/Moscow")
    return {"time": datetime.now(zone)}
