'''
Simple web application for showing current UTC+3 time
'''

import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_moscow_time():
    '''
    Root endpoint that shows time page
    '''
    moscow_time = get_moscow_time()
    return render_template('index.html', moscow_time=moscow_time)

def get_moscow_time():
    '''
    Function that receives UTC time and make offset with 3 hours
    '''
    # Get the current UTC time
    utc_time = datetime.datetime.utcnow()

    # Moscow is UTC+3, so add 3 hours to the UTC time
    moscow_time = utc_time + datetime.timedelta(hours=3)

    return moscow_time.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
