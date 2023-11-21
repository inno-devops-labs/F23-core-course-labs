from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pytz import timezone


app = FastAPI()
tz = timezone("Europe/Moscow")


@app.get("/")
def root():
    add_visit()
    return PlainTextResponse(datetime.now(tz).isoformat())


@app.get("/visits")
def show_visits():
    with open("storage/visits", 'r') as file:
        visits = file.read()
    return PlainTextResponse(f"The website was visited {visits} times")


def add_visit():
    with open("storage/visits", 'r') as file:
        visits = int(file.read())
    with open("storage/visits", 'w') as file:
        file.write(f"{visits + 1}")