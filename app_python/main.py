import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from .routers import time

STATIC_PATH = Path(os.path.dirname(os.path.realpath(__file__))) / "static"

app = FastAPI()
Instrumentator().instrument(app).expose(app)

app.include_router(time.router)

app.mount("/", StaticFiles(directory=STATIC_PATH, html=True), name="static")
