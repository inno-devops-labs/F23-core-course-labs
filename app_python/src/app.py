import pytz
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
tz = pytz.timezone('Europe/Moscow')


@app.get('/')
def get_current_time():
    time = str(datetime.now(tz))

    return HTMLResponse(text=f"<center>"f"<h1>{time}</h1>"f"</center>", content_type='text/html')
