import router as timer

import uvicorn
from fastapi import FastAPI
import logging

logging.basicConfig(
    format="%(asctime)-s  %(levelname)-8s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
app = FastAPI()

timerRouter = timer.TimeRouter("timerRouter", "/", logger)
app.include_router(timerRouter.router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=7098)


if __name__ == "__main__":
    main()
