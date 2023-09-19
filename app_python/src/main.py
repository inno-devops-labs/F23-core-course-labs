"""Main file to run"""
from datetime import datetime

import pytz
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    """Return Moscow time."""
    now = datetime.now(tz=pytz.timezone("Europe/Moscow"))

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
