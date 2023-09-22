from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.get('/')
def home():
    moscow_time = datetime.now(timezone('Europe/Moscow'))
    return render_template('base.html', moscow_time=moscow_time)