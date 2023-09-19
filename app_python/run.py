from datetime import datetime
import pytz
from flask import Flask


TIMEZONE = 'Europe/Moscow'
DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"


app = Flask(__name__)


@app.route('/')
def get_moscow_time():
    moscow_time = datetime.now(pytz.timezone(TIMEZONE))
    formatted_time = moscow_time.strftime(DATETIME_FORMAT)
    return formatted_time




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
