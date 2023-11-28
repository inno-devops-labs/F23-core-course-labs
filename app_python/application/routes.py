from flask import Blueprint, render_template
from prometheus_client import Counter
import datetime

bp = Blueprint("main", __name__)

REQUEST_COUNT = Counter(
    "app_request_count",
    "Application Request Count",
    ["method", "endpoint", "http_status"],
)


@bp.route("/")
def get_moscow_time():
    REQUEST_COUNT.labels("GET", "/", 200).inc()

    date = datetime.timezone(datetime.timedelta(hours=3))
    moscow_time = datetime.datetime.now(date)
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")

    with open("./volume/visits", "w") as file:
        file.write(str(REQUEST_COUNT.labels("GET", "/", 200)._value.get()))

    return render_template("index.html", time=formatted_time)


@bp.route("/visits")
def show_visits():
    return str(REQUEST_COUNT.labels("GET", "/", 200)._value.get())
