from flask import Flask
from datetime import datetime
from zoneinfo import ZoneInfo
from waitress import serve

app = Flask(__name__)


@app.route("/")
def current_time():
    moscow_zone_info = ZoneInfo("Europe/Moscow")
    time: datetime = datetime.now(tz=moscow_zone_info)
    time_str: str = time.strftime("%H:%M:%S")

    return "Moscow Time: " + time_str


if __name__ == "__main__":
    serve(app=app, port="8080")
