"""Main file to run"""
from datetime import datetime

import pytz
import uvicorn
from fastapi import FastAPI
from os.path import exists

VISIT_FILE = "data/visits.txt"

app = FastAPI()

def update_visit():
    if exists(VISIT_FILE):
        with open(VISIT_FILE, "r") as file:
            visits = int(file.read())
    else:
        visits = 0
    with open(VISIT_FILE, "w") as file:
        file.write(str(visits + 1))


def get_visits():
    if exists(VISIT_FILE):
        with open(VISIT_FILE, "r") as file:
            return int(file.read())
    else:
        return 0
    

@app.get("/visits")
async def visits():
    return get_visits()


@app.get("/")
async def home():
    """Return Moscow time."""
    now = datetime.now(tz=pytz.timezone("Europe/Moscow"))

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    update_visit()
    return dt_string


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
