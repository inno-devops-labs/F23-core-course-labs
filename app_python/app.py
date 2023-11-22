from fastapi import FastAPI
from datetime import datetime
import os
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

path = '/data/visits.txt'

def get_current_visits():
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                return int(file.read())
    except Exception as e:
        print(e)
    return 0

def update_visits():
    try:
        current_visits = get_current_visits()
        if os.path.exists(path):
            with open(path, 'w') as file:
                file.write(str(current_visits + 1))
    except Exception as e:
        print(e)
    return 0

@app.get('/visits')
def get_visits():
    return str(get_current_visits())

@app.get('/')
def display_msk_time():
    update_visits()
    msk_timezone = pytz.timezone('Europe/Moscow')
    return {"Current time in Moscow is": datetime.now(msk_timezone).strftime("%Y-%m-%d %H:%M:%S")}
