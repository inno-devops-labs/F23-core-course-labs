from datetime import datetime

from pytz import timezone

from fastapi import FastAPI

from app_python.src import config


app = FastAPI()


@app.get("/")
async def get_time():
    time = datetime.now(timezone(config.timezone))
    return {"current_time": time.strftime(config.time_format)}
