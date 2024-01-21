from flask import Flask
import datetime
import pytz

app = Flask(__name__)


@app.route('/')
def show_time():
    timezone = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(timezone)
    formatted_time = current_time.strftime('%H:%M:%S')
    return "Moscow Time: " + formatted_time


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
