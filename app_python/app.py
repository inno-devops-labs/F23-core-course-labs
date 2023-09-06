from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f'Current time in Moscow: {current_time}'


if __name__ == '__main__':
    app.run()
