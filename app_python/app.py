from datetime import datetime
from pytz import timezone
from flask import Flask

# Create the Flask app
app = Flask(__name__)

@app.route('/')
def index():
    """
    Handle the root endpoint.

    Returns:
        str: A string containing the current time in Moscow.
    """
    moscow_tz = timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%H:%M:%S')
    return f"Current time in Moscow: {current_time}"

if __name__ == '__main__':
    app.run(debug=True)