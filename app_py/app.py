from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return time.strftime('%A %B, %d %Y %H:%M:%S')