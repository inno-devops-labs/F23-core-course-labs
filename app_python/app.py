from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/', methods=["GET"])
def display_moscow_time():
    return get_moscow_time()

def get_moscow_time():
    # Get the current time in UTC
    utc_time = datetime.datetime.utcnow()
    moscow_offset = datetime.timedelta(hours=3) # Moscow is UTC+3 
    # Add the Moscow time offset to the UTC time
    moscow_time = utc_time + moscow_offset
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
