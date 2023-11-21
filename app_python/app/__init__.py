from flask import Flask
import datetime
import pytz

app = Flask(__name__)
filename = './volume/counter.txt'

def get_counter():
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        with open(filename, "w") as file:
            file.write('0')

    return 0

def inc():
    counter = int(get_counter()) + 1
    with open(filename, "w") as file:
        file.write(str(counter))

    return counter



@app.route('/')
def index():
    inc()

    utc_now = datetime.datetime.now(pytz.utc)
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_now = utc_now.astimezone(moscow_tz)
    moscow_time = moscow_now.strftime('%Y-%m-%d %H:%M:%S')

    return moscow_time

@app.route('/visits')
def counter():
    return str(get_counter())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
