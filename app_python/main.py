import logging
from flask import Flask
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
logging.basicConfig(
    format='[%(levelname)-8s] %(asctime)-s:\t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)


@app.route('/')
def current_time():
    # Get time in Moscow
    moscow_time = datetime.now(timezone(timedelta(hours=3)))
    logger.info(msg=f'Method: GET Response: {moscow_time}')
    return f'Current time in Moscow: {moscow_time.strftime("%H:%M:%S")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
