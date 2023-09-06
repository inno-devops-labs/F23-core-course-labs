from flask import Blueprint, render_template
from datetime import datetime, timedelta

blue = Blueprint('time', __name__)

utc = 3

@blue.route('/')
def time_in_moscow():
    moscow_date_time = datetime.utcnow() + timedelta(hours=utc)
    moscow_time = moscow_date_time.strftime("%d-%m-%Y\n" + "%H:%M:%S")

    return render_template('index.html', time= moscow_time)