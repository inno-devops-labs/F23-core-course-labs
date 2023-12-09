import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_tz)
    time = current_time.strftime('%H:%M:%S')
    visit_count = increment_visits()
    return render_template('index.html', time=time)


def read_visits():
    try:
        with open("visits.txt", "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0


def increment_visits():
    count = read_visits() + 1
    with open("visits.txt", "w+") as file:
        file.write(str(count))
    return count


@app.route('/visits')
def show_visits():
    visit_count = read_visits()
    return f"Number of visits: {visit_count}"
