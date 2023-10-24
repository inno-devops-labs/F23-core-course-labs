from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI, Response, status
from fastapi.responses import ORJSONResponse
from starlette.requests import Request
from app_python.config import config
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()

FORMAT = '%H:%M:%S'

instrumentator = Instrumentator().instrument(app)


@app.on_event('startup')
async def startup():
    instrumentator.expose(app)


@app.get("/")
async def root(request: Request):
    return config.templates.TemplateResponse(name="page.html",
                                             context={"request": request,
                                                      "Title": "DevOps lab",
                                                      "Msg": "Hello! This is DevOps course lab by Safina Alina",  # noqa: E501
                                                      "Href": "/time",
                                                      "LinkMsg": "Current time in Moscow"},  # noqa: E501
                                             status_code=200)


@app.get("/time")
async def time(request: Request):
    return config.templates.TemplateResponse(name="page.html",
                                             context={"request": request,
                                                      "Title": "DevOps lab",
                                                      "Msg": f"Current time in Moscow:"  # noqa: E501
                                                             f"{datetime.now(tz=ZoneInfo('Europe/Moscow')).strftime(FORMAT)}",  # noqa: E501
                                                      "Href": "/",
                                                      "LinkMsg": "Main page"},
                                             status_code=200)


@app.get("/health")
async def healthcheck(response: Response):
    response.status_code =  status.HTTP_200_OK
    return ORJSONResponse([{"status": "Ok"}])