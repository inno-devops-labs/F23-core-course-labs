from flask import Flask, render_template
import os
import datetime
import pytz

app = Flask(__name__)

volume_path = '/volume'
file_name = 'visits.txt'
path = os.path.join(volume_path, file_name)

def create_visits_file():
    with open(path, 'w') as file:
        file.write('0')

@app.route('/')
def display_time():
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                counter = file.read()
            with open(path, 'w') as file:
                counter = counter if counter else '0'
                file.write(str(int(counter) + 1))

            moscow_tz = pytz.timezone('Europe/Moscow')
            current_time = datetime.datetime.now(moscow_tz)
            formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
            return render_template('time.html', time=formatted_time)
        else:
            create_visits_file()
            return "Created visits.txt in the volume. Please refresh the page."
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")
        return "An error occurred"

@app.route('/visits')
def visits():
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                content = file.read()
                return str(int(content)) if content else "0"
        else:
            create_visits_file()
            return "Created visits.txt in the volume. Please refresh the page."
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return "An error occurred"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
