import uvicorn
from fastapi import FastAPI

import timer.router as timer

app = FastAPI()

timerRouter = timer.TimeRouter("timerRouter", "/")
app.include_router(timerRouter.router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=7098)
