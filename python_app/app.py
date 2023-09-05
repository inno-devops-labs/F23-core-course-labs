from datetime import datetime

import pytz
from flask import Flask, render_template

import config

app = Flask(__name__)


@app.route('/')
def index():
    current_time = get_current_time()
    print(current_time)

    return render_template('index.html', current_time=current_time)


def get_current_time():
    """ Getting formatted time in Moscow time-zone """

    moscow_timezone = pytz.timezone(config.time_zone)
    time = datetime.now(moscow_timezone)

    return time.strftime(config.time_format)


if __name__ == '__main__':
    app.run()
