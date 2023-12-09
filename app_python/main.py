"""
This module displays moscow time
"""
from datetime import datetime

import pytz
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_time():
    """
    Return moscow time as html
    """
    mtz = pytz.timezone("Europe/Moscow")
    time_in_moscow = datetime.now(mtz)
    time_formated = time_in_moscow.strftime("%H:%M:%S")

    return render_template('time.html', time=time_formated)

@app.errorhandler(404)
def not_found():
    """
    Return error page not found as html
    """
    return render_template("error.html"),404

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
