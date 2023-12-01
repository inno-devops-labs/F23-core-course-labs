import datetime
import os
from flask import Flask, render_template

key = "super_secret_key"
app = Flask(__name__)

def read_visits():
    '''
    Reads the number of visits from the file
    '''
    try:
        with open("/app/out/visits.txt", "r") as file:
            return int(file.read().strip())
    except Exception:
        return 0

def increment_visits():
    '''
    Increments the number of visits and saves it to the file
    '''
    count = read_visits() + 1
    with open("/app/out/visits.txt", "w") as file:
        file.write(str(count))
    return count

@app.route('/')
def show_moscow_time():
    '''
    Root endpoint that shows time page and increments visit count
    '''
    moscow_time = get_moscow_time()
    visit_count = increment_visits()
    return render_template('index.html', moscow_time=moscow_time)

@app.route('/visits')
def show_visits():
    '''
    Endpoint to show the number of visits
    '''
    visit_count = read_visits()
    return f"Number of visits: {visit_count}"

def get_moscow_time():
    '''
    Function that receives UTC time and makes an offset of 3 hours
    '''
    utc_time = datetime.datetime.utcnow()
    moscow_time = utc_time + datetime.timedelta(hours=3)
    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
