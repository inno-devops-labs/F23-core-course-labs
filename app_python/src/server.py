import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

from src.time_api.time_router import time_api_router

description = """
QUINER API helps you do awesome stuff. 🚀

## Time

You can get current Moscow time and data.
"""

app = FastAPI(
    title="QuinerApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Anatoliy Shvarts",
        "email": "a.shvarts@innopolis.university",
    },
)

instrumentator = Instrumentator().instrument(app)


@app.on_event('startup')
async def startup():
    instrumentator.expose(app)


app.include_router(time_api_router)


@app.get("/visits")
async def get_visits():
    visits_file_path = f"{os.path.dirname(os.path.realpath(__file__))}/../data/visits.txt"
    try:
        with open(visits_file_path, "r") as f:
            visits = f.readline().strip()
            if visits is None or visits == "":
                visits = 0
            else:
                visits = int(visits)
    except IOError:
        visits = 0

    return JSONResponse(content={"visits": visits}, status_code=200)

@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"message": "OK"}, status_code=200)
