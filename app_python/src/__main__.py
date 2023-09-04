import uvicorn
from fastapi import FastAPI

from app_python.src.time.time_router import time_router
from config import config

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
    }
)

app.include_router(time_router)


if __name__ == "__main__":
    uvicorn.run("__main__:app",
                host=config.host,
                port=config.port,
                reload=False)
