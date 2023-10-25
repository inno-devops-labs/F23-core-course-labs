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

    return render_template("index.html", time=formatted_time)
