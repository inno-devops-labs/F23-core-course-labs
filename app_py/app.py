from flask import Flask
import datetime
import pytz

app = Flask(__name__)
timezone = pytz.timezone('Europe/Moscow')
@app.route("/")
def hello_world():
    curTime = datetime.datetime.now(tz = timezone)
    return curTime.strftime('%Y-%m-%d %H:%M:%S')
