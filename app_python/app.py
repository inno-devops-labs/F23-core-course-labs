from config import LOG_LEVEL, LOG_FILENAME, LOG_MAX_BYTES, LOG_BACKUP_COUNT, LOG_FORMAT
from flask import Flask, render_template
from datetime import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler

# Set up file and console logging
logger = logging.getLogger()
logger.setLevel(LOG_LEVEL)

file_handler = RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=LOG_MAX_BYTES,
    backupCount=LOG_BACKUP_COUNT)
file_handler.setLevel(LOG_LEVEL)

console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)

formatter = logging.Formatter(LOG_FORMAT)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


app = Flask(__name__)


@app.route('/')
def moscow_time():
    try:
        # Fetch Moscow time
        moscow_tz = pytz.timezone('Europe/Moscow')
        current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
        app.logger.info('Moscow time fetched successfully.')

        # Render HTML
        return render_template("time.html", current_time=current_time)

    except Exception as e:
        app.logger.error(f"Error fetching Moscow time: {e}")
        return "Error fetching Moscow time", 500


if __name__ == "__main__":
    app.run(debug=True)
