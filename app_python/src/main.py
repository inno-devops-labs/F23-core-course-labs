from fastapi import FastAPI
from datetime import datetime
import pytz
import os
import threading

app = FastAPI()

mutex = threading.Lock()
visits_file_path = "data/visits"
os.makedirs("data", exist_ok=True)


@app.get("/visits")
async def check_visits():
    try:
        with open(visits_file_path, "r") as f:
            count = int(f.readline())
    except:
        count = 0
    return count


@app.get("/")
async def root():
    mutex.acquire()
    try:
        with open(visits_file_path, "r") as f:
            count = f.readline().strip()
            if count is None or count == "":
                count = 1
            else:
                count = int(count) + 1
    except IOError:
        count = 1
    with open(visits_file_path, "w") as f:
        f.writelines(str(count))
    mutex.release()
    return datetime.now(pytz.timezone('Europe/Moscow')).ctime()
