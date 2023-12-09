from flask import Flask, url_for, render_template, redirect
from timezone import get_moscow_time

app = Flask(__name__)

@app.route('/')
def main():
    (date, time) = get_moscow_time()
    return render_template('index.html', date=date, time=time)

@app.errorhandler(404)
def redirect_from_not_found(_error):
    return redirect(url_for('main'))
