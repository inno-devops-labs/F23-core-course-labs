from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def get_current_time():
    date_format = "%d/%m/%Y %H:%M:%S"
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    time = moscow_time.strftime(date_format)
    return "The current time in Moscow: %s" % time


if __name__ == '__main__':
    app.run()
