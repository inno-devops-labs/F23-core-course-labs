# Import necessary modules
import argparse
from waitress import serve
from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

# Create a Flask web application instance
app = Flask(__name__)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-prod", "--production", action='store_true')

# Define the Moscow time zone (UTC+3) for use in datetime calculations
MOSCOW_TZ = timezone(timedelta(hours=3))  # Moscow time zone (UTC+3)


# Define a route that displays the current Moscow time
@app.route('/')
def display_time():
    moscow_time = datetime.now(MOSCOW_TZ).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', moscow_time=moscow_time)


# Entry point for the script
if __name__ == '__main__':
    is_prod = parser.parse_args().production

    if is_prod:
        serve(app, port=80)
    else:
        app.run()
