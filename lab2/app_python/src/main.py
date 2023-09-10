from fastapi import FastAPI
from datetime import datetime
from pytz import timezone

app = FastAPI()


@app.get("/")
async def get_current_moscow_time():
    time = datetime.now(timezone('Europe/Moscow'))
    return time.strftime("%H:%M:%S")
