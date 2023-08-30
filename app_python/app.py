from datetime import datetime, timezone, timedelta
from flask import Flask, render_template

MSK_TIMEZONE = timezone(timedelta(hours=3))

app = Flask(__name__)


@app.route('/')
def show_time():
    # Get current time in Moscow timezone
    time_now = datetime.now(MSK_TIMEZONE).strftime('%H:%M:%S')
    return render_template('index.html', current_time=time_now)


if __name__ == '__main__':
    app.run()
