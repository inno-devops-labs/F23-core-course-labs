from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app_python/templates")
FORMAT = '%H:%M:%S'


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(name="page.html",
                                      context={"request": request,
                                               "Title": "Lab 2",
                                               "Msg": "Hello! This is DevOps course lab 2 by Safina Alina",  # noqa: E501
                                               "Href": "/time",
                                               "LinkMsg": "Current time in Moscow"},  # noqa: E501
                                      status_code=200)


@app.get("/time")
async def time(request: Request):
    return templates.TemplateResponse(name="page.html",
                                      context={"request": request,
                                               "Title": "Lab 2",
                                               "Msg": f"Current time in Moscow:"  # noqa: E501
                                                      f"{datetime.now(tz=ZoneInfo('Europe/Moscow')).strftime(FORMAT)}",  # noqa: E501
                                               "Href": "/",
                                               "LinkMsg": "Main page"},
                                      status_code=200)
