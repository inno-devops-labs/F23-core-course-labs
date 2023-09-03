from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

EMAIL = "s.khamrakulov@innopolis.university"
ID_BASE_URL = "https://fwd.innopolis.app/api/hw2"
COMIC_BASE_URL = "https://getxkcd.vercel.app/api/comic"


def get_id() -> int:
    response = requests.get(f"{ID_BASE_URL}?email={EMAIL}")
    response_body = response.json()
    return response_body


def get_comic() -> dict:
    id = get_id()
    response = requests.get(f"{COMIC_BASE_URL}?num={id}")
    response_body = response.json()
    return response_body


@app.route("/")
def index():
    # Fetch a random XKCD comic from the API
    comic = get_comic()

    return render_template("index.html", comic=comic)


@app.route("/refresh", methods=["GET"])
def refresh_comic():
    # Fetch a new random XKCD comic from the API
    comic = get_comic()
    return jsonify(comic)


if __name__ == "__main__":
    app.run(debug=True)
