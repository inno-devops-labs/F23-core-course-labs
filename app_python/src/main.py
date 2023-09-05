from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/")
async def root():
    return datetime.now(pytz.timezone('Europe/Moscow')).ctime()
