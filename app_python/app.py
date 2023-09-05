from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def index():
    tz = pytz.timezone("Europe/Moscow")
    current_time: datetime = datetime.now(tz)
    current_time_formatted: str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return f"The current time in Moscow is: {current_time_formatted}"