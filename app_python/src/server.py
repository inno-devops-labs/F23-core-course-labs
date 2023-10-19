from fastapi import FastAPI
from fastapi.responses import JSONResponse

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

app.include_router(time_api_router)


@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"message": "OK"}, status_code=200)
