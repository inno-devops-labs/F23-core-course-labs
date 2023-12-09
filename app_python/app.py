import falcon
from datetime import datetime, timezone, timedelta

class MoscowTime:
    def on_get(self, req, resp):
        tz = timezone(timedelta(hours=3))
        resp.text = datetime.now(tz).strftime('%a %d %b %Y, %I:%M:%S %p')
        try:
            with open('visits', 'r') as f:
                visits = int(f.read())
        except FileNotFoundError:
            visits = 0
        
        with open('visits', 'w') as f:
            f.write(str(visits + 1))


class GetVisits:
    def on_get(self, req, resp):
        try:
            with open('visits', 'r') as f:
                resp.text = f.read()
        except FileNotFoundError:
            resp.text = '0'


def create():
    app = falcon.App()
    app.add_route('/', MoscowTime())
    app.add_route('/visits', GetVisits())
    return app


app = create()
