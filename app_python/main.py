from flask import Flask
from datetime import datetime
import pytz

path_visits = "./volume/visits"

app = Flask(__name__)


def visits_read():
    return int(open(path_visits, "r").read())

def visits_write(visits):
    new_file = open(path_visits, "w")
    new_file.write(str(visits))
    new_file.close()

@app.route('/')
def moscow_time():
    visits_write(visits_read() + 1)
    timezone = pytz.timezone('Europe/Moscow')
    time = datetime.now(timezone)
    formatted_time = time.strftime('%Y-%m-%d, %H:%M:%S.%f')[:-3]
    return 'Current Moscow time is ' + formatted_time

@app.route("/visits")
def get_visits():
    return str(visits_read())

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)