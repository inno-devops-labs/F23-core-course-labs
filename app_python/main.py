import uvicorn
from fastapi import FastAPI
import pytz
from datetime import datetime

app = FastAPI()


@app.get("/")
async def home():
    now = datetime.now(tz=pytz.timezone('Europe/Moscow'))

    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
