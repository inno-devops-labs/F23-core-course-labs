from datetime import datetime
from pytz import timezone

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import config


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


def format_time(time: datetime):
    return time.astimezone(config.timezone).strftime(config.time_format)


@app.get('/time', response_class=HTMLResponse)
def get_time(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'time': format_time(datetime.now(timezone('UTC')))
    })
