"""Python devops app"""
from datetime import datetime
import pytz

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def show_time():
    """Function printing Moscow time"""
    msk_time = datetime.now(pytz.timezone('Europe/Moscow'))
    formatted_time = msk_time.strftime('%H:%M:%S')

    with open("data/visits.txt", "r") as f:
        visits = int(f.read()) + 1

    with open("data/visits.txt", "w") as f:
        f.write(str(visits))

    html_content = """
            <html>
                <head>
                    <title>Current Time Check</title>
                </head>
                <body>
                    <h1>Moscow time</h1>
                    <h3>Current time in Moscow is %s</h3>
                </body>
            </html>
            """

    return HTMLResponse(content=html_content % formatted_time, status_code=200)


@app.get("/visits")
async def show_visits():
    """Function printing number of visits"""
    with open("data/visits.txt", "r") as f:
        v = f.readline()

    html_content = """
            <html>
                <head>
                    <title>Current Visits Check</title>
                </head>
                <body>
                    <h1>Visits of Time Check</h1>
                   <p>Number of visits: %s </p>
                </body>
            </html>
            """

    return HTMLResponse(content=html_content % v, status_code=200)
