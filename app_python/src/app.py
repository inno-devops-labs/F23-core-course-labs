import pytz
from fastapi import FastAPI
from pathlib import Path
from datetime import datetime

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
    increment_visitor_count()

    ts = datetime.now()
    return {'timestamp': tz.localize(ts).isoformat()}

@app.get('/visitors')
def get_visitors():
    return {'count': get_visitor_count()}
