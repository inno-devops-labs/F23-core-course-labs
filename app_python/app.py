from datetime import datetime
from flask import Flask, render_template
import pytz
from waitress import serve


# Функция, которая возвращает время в определенном месте (в формате %H:%M:%S)
def get_timezone(name):
    return datetime.now(pytz.timezone(name)).strftime('%H:%M:%S')


# Создаем Flask app
app = Flask(__name__)


@app.route('/')
def main():
    current_time = get_timezone('Europe/Moscow')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    serve(app, port=8080)
