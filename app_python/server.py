from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from app_python.config import config

app = FastAPI()

FORMAT = '%H:%M:%S'


@app.get("/")
async def root(request: Request):
    return config.templates.TemplateResponse(name="page.html",
                                                 context={"request": request,
                                                          "Title": "DevOps lab",
                                                          "Msg": "Hello! This is DevOps course lab by Safina Alina",
                                                          # noqa: E501
                                                          "Href": "/time",
                                                          "LinkMsg": "Current time in Moscow"},  # noqa: E501
                                                 status_code=200)


@app.get("/time")
async def time(request: Request):
    return config.templates.TemplateResponse(name="page.html",
                                             context={"request": request,
                                                      "Title": "DevOps lab",
                                                      "Msg": f"Current time in Moscow:"  # noqa: E501
                                                             f"{datetime.now(tz=ZoneInfo('Europe/Moscow')).strftime(FORMAT)}",
                                                      # noqa: E501
                                                      "Href": "/",
                                                      "LinkMsg": "Main page"},
                                             status_code=200)
