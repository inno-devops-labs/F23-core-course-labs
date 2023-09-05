import requests
import json
import calendar
from flask import Flask

app = Flask(__name__)

@app.route('/')
def MoscowTime():
    response = requests.get('https://api.api-ninjas.com/v1/worldtime?city={}'.format("Moscow"), timeout=5,
                            headers={'X-Api-Key': 'oZDQTEM0MJpKNshpblkFBQ==RRsPxd52ToPtLq75'})

    if response.status_code == requests.codes.ok:
        res = json.loads(response.text)
        time = res['hour']+":"+res['minute']+":"+res['second']+", "+res['day']+" "+\
               str(calendar.month_name[int(res['month'])])+" "+\
               res['year']+", "+res['day_of_week']
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Moscow Time App</title>
            </head>
            <body>
               <h1>Current Moscow Time is</h1>
               <h2> """+time+""" </h2>
            </body>
            </html>
        """
    return """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Moscow Time App</title>
                </head>
                <body>
                   <h1>Error occurred while loading a Moscow Time</h1>
                </body>
                </html>
            """

app.run()
