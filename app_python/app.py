from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)


def get_timezone(name):
    return datetime.now(pytz.timezone(name)).strftime('%H:%M:%S')


@app.route('/')
def main():
    current_time = get_timezone('Europe/Moscow')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run()
