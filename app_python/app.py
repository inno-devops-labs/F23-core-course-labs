from fastapi import FastAPI
from datetime import datetime
import pytz
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator().instrument(app).expose(app)

@app.get('/')
def display_msk_time():
    msk_timezone = pytz.timezone('Europe/Moscow')
    return {"Current time in Moscow is": datetime.now(msk_timezone).strftime("%Y-%m-%d %H:%M:%S")}
