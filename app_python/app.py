from datetime import datetime
import logging
from flask import Flask, render_template
import pytz
from waitress import serve

logging.basicConfig(
    format='%(levelname)-8s -- %(asctime)-s -- Message: \t%(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

logger = logging.getLogger("waitress")
logger.setLevel(logging.INFO)


# Функция, которая возвращает время в определенном месте (в формате %H:%M:%S)
def get_timezone(name):
    return datetime.now(pytz.timezone(name)).strftime('%H:%M:%S')


# Создаем Flask app
app = Flask(__name__)


@app.route('/')
def main():
    current_time = get_timezone('Europe/Moscow')
    logger.info(msg=f'Route: /')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    serve(app, port=8080)
