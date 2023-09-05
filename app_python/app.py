from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

MOSCOW_TZ = pytz.timezone('Europe/Moscow')

def get_moscow_time():
    cur_time = datetime.now(MOSCOW_TZ)
    return cur_time.strftime("%Y-%m-%d %H:%M:%S")

@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
