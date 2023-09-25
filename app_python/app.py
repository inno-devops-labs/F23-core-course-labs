"""
Main file for Moscow Time application
"""

from datetime import datetime
from flask import Flask, render_template
import pytz

app = Flask(__name__)

@app.route('/')
def index():
    """Route gets time and returns template page with time variable"""
    moscow_time = get_time()
    return render_template('index.html', time=moscow_time)

@app.route('/time')
def get_time():
    """Route provides Moscow time"""
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone).strftime('%Y-%m-%d %H:%M:%S')
    return moscow_time


if __name__ == '__main__':
    app.run()
