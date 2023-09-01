from flask import Flask, render_template
import datetime
import pytz

app = Flask(__name__)


def get_moscow_time():
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.datetime.now(moscow_timezone)
    return moscow_time.strftime("%Y-%m-%d %H:%M:%S")


@app.route("/")
def show_time():
    moscow_time = get_moscow_time()
    return render_template("index.html", moscow_time=moscow_time)


@app.route("/get_time/")
def get_time():
    moscow_timezone = pytz.timezone("Europe/Moscow")
    moscow_time = datetime.datetime.now(moscow_timezone)
    formatted_time = moscow_time.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time


if __name__ == "__main__":
    app.run(debug=True)
