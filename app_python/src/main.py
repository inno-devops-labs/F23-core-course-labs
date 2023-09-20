import router as timer

import uvicorn
from fastapi import FastAPI

app = FastAPI()

timerRouter = timer.TimeRouter("timerRouter", "/")
app.include_router(timerRouter.router)


def main():
    uvicorn.run(app, host="0.0.0.0", port=7098)


if __name__ == "__main__":
    main()
