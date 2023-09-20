import falcon
from datetime import datetime, timezone, timedelta


class MoscowTime:
    def on_get(self, req, resp):
        tz = timezone(timedelta(hours=3))
        resp.text = datetime.now(tz).strftime('%a %d %b %Y, %I:%M:%S %p')


def create():
    app = falcon.App()
    app.add_route('/', MoscowTime())
    return app


app = create()
