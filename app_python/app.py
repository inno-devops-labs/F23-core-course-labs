from datetime import datetime, timedelta, timezone

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    curr_time = datetime.now(timezone(timedelta(hours=3))).strftime('%H:%M:%S')
    return render_template('index.html', curr_time=curr_time)


if __name__ == '__main__':
    app.run()
