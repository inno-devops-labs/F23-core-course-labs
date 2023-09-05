from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

MOSCOW_TZ = timezone(timedelta(hours=3))  # Moscow time zone (UTC+3)


@app.route('/')
def display_time():
    moscow_time = datetime.now(MOSCOW_TZ).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', moscow_time=moscow_time)


if __name__ == '__main__':
    app.run()
