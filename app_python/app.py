from datetime import datetime, timedelta, timezone
from waitress import serve

from flask import Flask, render_template
import logging

logging.basicConfig(
    format='[%(levelname)-8s] %(asctime)-s:\t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)

app = Flask(__name__)

@app.route('/')
def main():
    curr_time = datetime.now(timezone(timedelta(hours=3))).strftime('%H:%M:%S')
    logger.info(msg=f'Method: GET Response: {curr_time}')
    return render_template('index.html', curr_time=curr_time)

if __name__ == '__main__':
    serve(app, port=8090)
    # app.run(port=8090)