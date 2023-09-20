from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.testclient import TestClient
from datetime import datetime
from .config import timezone
import pytz
import os

app = FastAPI()


def get_test_client():
 return TestClient(app)


TEMPLATES_PATH = os.path.join(
    os.path.dirname(__file__),
    'templates',
)
templates = Jinja2Templates(directory=TEMPLATES_PATH)


@app.get(
    '/',
    response_class=HTMLResponse,
)
async def get_current_time(request: Request):

    moscow_tz = pytz.timezone(zone=timezone)
    current_time = datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%H:%M:%S')

    return templates.TemplateResponse(
        'current_time.html',
        {
            'request': request,
            'current_time': formatted_time,
        }
    )
