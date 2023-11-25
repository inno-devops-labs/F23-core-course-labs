from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# Initialize visit counter
visits_count = 0

def get_visits():
    counter = 0
    try:
        counter = int(open('visits.txt', 'r').read().strip())
    except Exception:
        pass

    return counter

@app.route('/')
def show_time():
    global visits_count
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    visits_count += 1  # Increment visit count for each request
    with open('visits.txt', 'w') as visits_file:  # Save visit count to a file
        visits_file.write(str(visits_count))
    return f'Current time in Moscow: {current_time}'

@app.route('/visits')
def visits():
    return f'Total visits: {get_visits()}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
