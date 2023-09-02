from flask import Blueprint, render_template
from datetime import datetime

time_blueprint = Blueprint('time', __name__)


@time_blueprint.route('/')
def current_time():
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('current_time.html', time=time_now)
