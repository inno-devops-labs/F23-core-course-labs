from flask import Flask, render_template
import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def display_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(moscow_tz)
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    return render_template('time.html', time=formatted_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
