"""
This module provides a simple web application that displays the current time in Moscow.

It utilizes the Flask framework for web development and serves the Moscow time on an HTML page.
"""

import os
import argparse
from datetime import datetime, timezone, timedelta
from waitress import serve
from flask import Flask, render_template

# Create a Flask web application instance
app = Flask(__name__)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-prod", "--production", action='store_true')

# Define the Moscow time zone (UTC+3) for use in datetime calculations
MOSCOW_TZ = timezone(timedelta(hours=3))  # Moscow time zone (UTC+3)
visits_file_path = "./volume/visits"
os.makedirs("volume", exist_ok=True)


# Define a route that displays the current Moscow time
@app.route('/')
def display_time():
    """
    Display the current time in Moscow.

    Returns:
        str: A string representing the current time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    with open(visits_file_path, 'r') as f:
        visits = int(f.read()) + 1

    with open(visits_file_path, 'w') as f:
        f.write(str(visits))
    moscow_time = datetime.now(MOSCOW_TZ).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', moscow_time=moscow_time)


@app.route("/visits")
def get_visits():
    with open(visits_file_path, 'r') as f:
        visits = f.read()

    return app.response_class(
        response=str(visits),
        status=200,
        mimetype="text/plain"
    )


# Entry point for the script
if __name__ == '__main__':
    is_prod = parser.parse_args().production

    if is_prod:
        serve(app, port=80)
    else:
        app.run()
