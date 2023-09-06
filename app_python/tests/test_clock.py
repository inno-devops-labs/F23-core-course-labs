from flask import Flask
import json
from datetime import datetime, timedelta
from app_python.config import config
from app_python.handlers.routes import configure_routes


def test_clock():
    app = Flask(__name__)
    configure_routes(app)    
    client = app.test_client()
    url: str = '/'
    tz = config["TZ"]
    threshold: datetime = timedelta(seconds=1)
    n_runs: int = 5


    for i in range(n_runs):
        now_real: datetime = datetime.now(tz=tz)
        response = client.get(url)
        now_returned = datetime.strptime(bytes.decode(response.get_data()), config["FORMAT"])
        now_returned = tz.localize(now_returned)
        

        assert (now_returned - now_real)  < threshold


