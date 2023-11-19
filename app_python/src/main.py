"""App Python main file that runs FastAPI"""
import threading
from datetime import datetime

from fastapi import FastAPI, status, Response
from prometheus_fastapi_instrumentator import Instrumentator
from pytz import timezone

from app_python.src import config

app = FastAPI()
mutex = threading.Lock()
visits_file_path = "data/visits"


@app.get("/")
async def get_time():
    """Provides current Moscow time on main route and updates visits counter"""
    mutex.acquire()
    try:
        with open(visits_file_path, "r") as f:
            visits = f.readline().strip()
            if visits is None or visits == "":
                visits = 1
            else:
                visits = int(visits) + 1
    except IOError:
        visits = 1
    with open(visits_file_path, "w") as f:
        f.writelines(str(visits))
    mutex.release()

    time = datetime.now(timezone(config.TIMEZONE))
    return {"current_time": time.strftime(config.TIME_FORMAT)}


@app.get("/visits")
async def check_visits():
    """Read file with counter and show the value to user"""
    try:
        with open(visits_file_path, "r") as f:
            visits = int(f.readline())
    except:
        visits = 0
    return visits


@app.get("/healthz")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)


@app.on_event('startup')
async def startup():
    Instrumentator().instrument(app).expose(app)
