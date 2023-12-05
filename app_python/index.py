from flask import Flask
import pytz
import os
from datetime import datetime

app = Flask(__name__)
PATH = "./volume/visits.txt"

def get_counter():
    if not os.path.exists(PATH):
        print(0, end='', file=open(PATH, 'w'))
        return 0
    else:
        counts = 0
        try:
            counts = int(open(PATH, 'r').read().strip())
        except Exception:
            pass
        return counts
@app.route('/')
def index():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    try:
        cnt = get_counter() + 1
        print(cnt, end='', file=open(PATH, 'w'))
    except Exception as e:
        print(f"Errors when write the file: {e}")
    return f"{current_time.strftime('%Y:%m:%d %H:%M:%S')}"

@app.route('/visits')
def visits():
    return f"{get_counter()}"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
