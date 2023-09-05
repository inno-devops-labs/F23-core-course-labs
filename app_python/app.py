from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def show_time():
    moscow_time = datetime.datetime.now(datetime.timezone.utc).astimezone(
        datetime.timezone(datetime.timedelta(hours=3))
    )
    return f'Current time in Moscow: {moscow_time.strftime("%Y-%m-%d %H:%M:%S")}'


if __name__ == "__main__":
    app.run()
