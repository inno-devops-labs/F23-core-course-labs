import uvicorn
from fastapi import FastAPI

from app_python.src.time.time_router import time_router
from config import config


app = FastAPI()

app.include_router(time_router)


if __name__ == "__main__":
    uvicorn.run("__main__:app",
                host=config.host,
                port=config.port,
                reload=False)
