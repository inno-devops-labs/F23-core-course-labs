import argparse
from datetime import datetime, timezone, timedelta
from flask import Flask, render_template
from waitress import serve

MSK_TIMEZONE = timezone(timedelta(hours=3))

app = Flask(__name__)
parser = argparse.ArgumentParser()

parser.add_argument("-prod", "--production", action='store_true')


@app.route('/')
def show_time():
    # Get current time in Moscow timezone
    time_now = datetime.now(MSK_TIMEZONE).strftime('%H:%M:%S')
    return render_template('index.html', current_time=time_now)


if __name__ == '__main__':
    is_prod = parser.parse_args().production

    if is_prod:
        serve(app, port=8000)
    else:
        app.run()
