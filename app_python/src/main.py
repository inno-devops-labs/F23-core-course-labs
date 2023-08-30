from datetime import datetime

from fastapi import FastAPI
from pytz import timezone

app = FastAPI()


@app.get("/")
def get_time():
    moscow = timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow)
    return {"time": moscow_time.strftime("%Y-%m-%d %H:%M:%S")}
