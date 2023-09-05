from datetime import datetime
import os

import pytz
from flask import Flask, request, render_template


"""create an instance of the Flask class"""
app = Flask(__name__)
LOGS = False


def get_current_time():
    """A simple function that returns current moscow time in "%H:%M:%S" format"""
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_timezone)
    return str(moscow_time.strftime("%H:%M:%S"))
    

@app.route('/')
def show_moscow_time():
    """Function that's render index.html template with current moscow time"""
    moscow_time = get_current_time()
    # This part for saving request addresses
    if not os.path.exists('/home/app/data/visits.txt'):
        if LOGS:
            print('ERROR: visits file not found')
    else:
        with open("/home/app/data/visits.txt", "a+") as f:
            f.write(f"{moscow_time} - {request.remote_addr}\n")

    return render_template("index.html", moscow_time=moscow_time)


@app.route("/get_time/")
def get_time():
    """Function for update time in loaded page"""
    return get_current_time()


@app.route('/visits')
def visits():
    """Function for send saved request addresses history"""
    
    try:
        web_content = "History:\n"
        with open("/home/app/data/visits.txt", "r") as fo:
            file_text = fo.read()
            web_content += f"{file_text}"
    except FileNotFoundError:
        web_content = 'ERROR: visits file not found'

    return web_content


if __name__ == '__main__':
    """call function from instance of the Flask class to start server"""
    app.run()
    LOGS = True