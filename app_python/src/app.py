import os
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

if not os.path.exists(config.visitors_path):
    open(config.visitors_path, 'w').write(str(0))


def get_visitors():
    with open(config.visitors_path, 'r') as f:
        return int(f.read())


def inc_visitors():
    vis = get_visitors()
    with open(config.visitors_path, 'w') as f:
        f.write(str(vis + 1))


def format_time(time: datetime):
    return time.astimezone(config.timezone).strftime(config.time_format)


@app.get('/time', response_class=HTMLResponse)
async def get_time(request: Request):
    inc_visitors()

    return templates.TemplateResponse('index.html', {
        'request': request,
        'time': format_time(datetime.now(timezone('UTC')))
    })


@app.get('/visitors', response_class=HTMLResponse)
async def get_time(request: Request):
    inc_visitors()

    return templates.TemplateResponse('visitors.html', {
        'request': request,
        'visitors_count': get_visitors()
    })
