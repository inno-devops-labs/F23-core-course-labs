from flask import Blueprint, render_template
import datetime

bp = Blueprint("main", __name__)


@bp.route("/")
def get_moscow_time():
    date = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(date)
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=formatted_time)
