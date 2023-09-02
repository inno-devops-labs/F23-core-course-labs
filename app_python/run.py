from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def current_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return f"The current time in Moscow is: {moscow_time}"

if __name__ == '__main__':
    app.run()