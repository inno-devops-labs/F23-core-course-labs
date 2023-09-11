import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_tz)
    time = current_time.strftime('%H:%M:%S')
    return render_template('index.html', time=time)
