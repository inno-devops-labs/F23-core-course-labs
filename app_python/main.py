from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)


@app.route('/')
def current_time():
    # Get time in Moscow
    moscow_time = datetime.now(timezone(timedelta(hours=3)))
    return f'Current time in Moscow: {moscow_time.strftime("%H:%M:%S")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
