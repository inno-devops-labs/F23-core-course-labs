import router as timer

import uvicorn
from fastapi import FastAPI
import logging

from prometheus_fastapi_instrumentator import Instrumentator

import visits_counter as VisitsRouter

logging.basicConfig(
    format="%(asctime)-s  %(levelname)-8s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
app = FastAPI()

visitsCounter = VisitsRouter.VisitsCounter('/home/python_runner/python/src/app/app_python/volume/visits.txt')

print('file found')

visitsRouter = timer.VisitsRouter("visitRouter", "/visits",visitsCounter )
timerRouter = timer.TimeRouter("timerRouter", "/", visitsCounter, logger)
app.include_router(timerRouter.router)
app.include_router(visitsRouter.router)


def main():
    Instrumentator().instrument(app).expose(app)
    uvicorn.run(app, host="0.0.0.0", port=7098)


if __name__ == "__main__":
    main()
