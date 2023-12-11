from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')  #the decorator registers the url
def index():
    record_visit()
    moscow_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=3)).strftime("%H:%M:%S")  # creates a string constraining in the current time in the format "hour:minutes:seconds"
    return render_template('index.html', moscow_time=moscow_time)

@app.route('/visits')  #the decorator registers the url
def visits():
    return str(record_visit())

def record_visit(): 
    with open('data/visits', 'r') as f:
        count = f.read()
        if count == '': 
            count = 0
        else: 
            count = int(count) 
    with open('data/visits', 'w') as f: 
        f.flush() 
        f.write(str(count + 1))
    return count 

if __name__ == '__main__':
    app.run(debug=True)
