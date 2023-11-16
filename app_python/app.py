from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

PATH = "volume/visits.txt"


@app.get('/')
def home():
    moscow_time = datetime.now(timezone('Europe/Moscow'))
    with open(PATH, 'a') as f:
        f.write(str(moscow_time))
        f.write('\n')

    return render_template('base.html', moscow_time=moscow_time)


@app.route("/visits")
def visits():
    with open(PATH, 'r') as f:
        visits = f.readlines()
    return '\n'.join(visits)
