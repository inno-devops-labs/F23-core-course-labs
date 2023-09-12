import argparse
from waitress import serve
from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument("-prod", "--production", action='store_true')

MOSCOW_TZ = timezone(timedelta(hours=3))  # Moscow time zone (UTC+3)


@app.route('/')
def display_time():
    moscow_time = datetime.now(MOSCOW_TZ).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', moscow_time=moscow_time)


if __name__ == '__main__':
    is_prod = parser.parse_args().production

    if is_prod:
        serve(app, port=80)
    else:
        app.run()
