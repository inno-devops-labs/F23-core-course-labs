from flask import Flask
import pytz
from datetime import datetime

app = Flask(__name__)
PATH = "./volume/visits.txt"

@app.route('/')
def index():
    moscow_tz = pytz.timezone("Europe/Moscow")
    current_time = datetime.now(moscow_tz)
    try:
        with open(PATH, "a+") as f:
            f.write(str(current_time))
            f.write('\n')
    except Exception as e:
        print(f"Errors when write the file: {e}")
    return f"{current_time.strftime('%Y:%m:%d %H:%M:%S')}"

@app.route('/visits')
def visits():
    try:
        with open(PATH, 'r') as f:
            v = f.readlines()
        return f"{len(v)}"
    except Exception as e:
        print(f"Error when read the file: {e}")
    return "empty"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
