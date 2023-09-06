import uvicorn
from fastapi import FastAPI

import app_python.src.timer.router as timer

app = FastAPI()

timerRouter = timer.TimeRouter("timerRouter", "/")
app.include_router(timerRouter.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7098)
