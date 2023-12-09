import pytz
from pathlib import Path
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

tz = pytz.timezone('Europe/Moscow')
data_path = Path('./data')
visitors_path = data_path.joinpath('visitors')

data_path.mkdir(exist_ok=True)
visitors_path.touch(exist_ok=True)

app = FastAPI()


def get_visitor_count():
    with open(visitors_path, 'r') as f:
        try:
            return int(f.read())
        except ValueError:
            return 0


def increment_visitor_count():
    current = get_visitor_count()
    with open(visitors_path, 'w') as f:
        f.write(str(current + 1))


@app.get('/')
def get_current_time():
    time = str(datetime.now(tz))

    return HTMLResponse(text=f"<center>"f"<h1>{time}</h1>"f"</center>", content_type='text/html')


@app.get('/visitors')
def get_visitors():
    return {'count': get_visitor_count()}
