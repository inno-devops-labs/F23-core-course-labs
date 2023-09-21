from flask import Flask, render_template
import datetime
import pytz

app = Flask(__name__)


@app.route("/")
def time_in_msk():  # put application's code here
    msk_timezone = pytz.timezone("Europe/Moscow")
    current_date = datetime.datetime.now(msk_timezone).strftime("%Y-%m-%d")
    current_time = datetime.datetime.now(msk_timezone).strftime("%H:%M:%S")
    return render_template(
        "index.html", current_date=current_date, current_time=current_time
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
