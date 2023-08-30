from datetime import datetime
from flask import Flask
import pytz


"""create an instance of the Flask class"""
app = Flask(__name__)


@app.route('/')
def show_moscow_time():
    """A simple function that returns current moscow time in "%H:%M:%S" format"""
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return str(moscow_time.strftime("%H:%M:%S"))


if __name__ == '__main__':
    """call function from instance of the Flask class to start server"""
    app.run()