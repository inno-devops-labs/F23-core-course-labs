from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

app = FastAPI()


@app.get("/")
async def read_main():
    current_time = datetime.now(tz=ZoneInfo(
        "Europe/Moscow")).strftime("%d/%m/%Y %H:%M:%S")
    return f"Hello, User! The date and time: {current_time}"
