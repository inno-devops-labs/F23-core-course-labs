from datetime import datetime
from threading import Lock

from flask import Flask, render_template
import pytz
from pydantic import BaseModel

app = Flask(__name__)
visits_data_file_path = 'data/visits_data.json'
visits_data_lock = Lock()


class VisitsData(BaseModel):
    visited_count: int = 0


def moscow_time() -> str:
    msk_tz = pytz.timezone('Europe/Moscow')
    time_str = datetime.now(msk_tz).strftime('%Y-%m-%d %H:%M:%S')

    return time_str


@app.route("/")
def homepage():
    visits_data_lock.acquire()
    try:
        with open(visits_data_file_path, 'r') as f:
            visits_data = VisitsData.model_validate_json(f.read())
    except FileNotFoundError:
        visits_data = VisitsData()
    
    visits_data.visited_count += 1
    with open(visits_data_file_path, 'w') as f:
        f.write(visits_data.model_dump_json())
    visits_data_lock.release()

    return render_template('index.html', time_str=moscow_time())


@app.route("/visits")
def visits():
    try:
        with open(visits_data_file_path, 'r') as f:
            visits_data = VisitsData.model_validate_json(f.read())
    except FileNotFoundError:
        visits_data = VisitsData()

    return render_template('visits.html', visits=visits_data.visited_count)
