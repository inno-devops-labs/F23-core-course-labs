import falcon
from datetime import datetime, timezone, timedelta

class MoscowTime:
    def on_get(self, req, resp):
        tz = timezone(timedelta(hours=3))
        resp.text = str(datetime.now(tz))

app = falcon.App()
app.add_route('/', MoscowTime())
