from flask import Flask, url_for, render_template, redirect
from timezone import get_moscow_time

app = Flask(__name__)

FILE = '/data/visits'

@app.route('/')
def main():
    (date, time) = get_moscow_time()
    try:
        with open(FILE, 'r') as f:
            visits = int(f.read())
    except:
        visits = 0

    with open(FILE, 'w') as f:
        f.write(str(visits + 1))

    return render_template('index.html', date=date, time=time)

@app.route('/visits')
def get_visits():
    visits = 0
    try:
        with open(FILE, 'r') as f:
            visits = int(f.read())
    except FileNotFoundError:
        visits = 0
    
    return {'visits': visits}

@app.errorhandler(404)
def redirect_from_not_found(_error):
    return redirect(url_for('main'))
