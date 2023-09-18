from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get('/')
def display_msk_time():
    msk_timezone = pytz.timezone('Europe/Moscow')
    return {"Current time in Moscow is": datetime.now(msk_timezone).strftime("%Y-%m-%d %H:%M:%S")}
