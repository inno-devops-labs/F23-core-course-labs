"""This module initializes a blueprint that serves current date and time to the user"""
from flask import Blueprint, render_template
from app.utils.time import moscow_time


time_blueprint = Blueprint('time', __name__)


@time_blueprint.route('/')
def current_time():
    """Implementation to GET request of date and time """

    time_now = moscow_time().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('current_time.html', time=time_now)
