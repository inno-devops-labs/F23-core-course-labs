import datetime
import pytz
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_time():
    return render_template('index.html')