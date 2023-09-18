from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi.testclient import TestClient

from app_python.config import config
from app_python.server import app
from app_python.templates import templates

client = TestClient(app)


def test_main():
    config.templates = templates.SetUpTemplates("../templates")
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    assert response.content.decode() == '''<!DOCTYPE html>
<html>
    <head>
        <title>DevOps lab</title>
    </head>
    <body>
        <h1>Hello! This is DevOps course lab by Safina Alina</h1>
        <h3>&#x2022; <a href=/time>Current time in Moscow</a> </h3>
    </body>
</html>'''


def test_time():
    config.templates = templates.SetUpTemplates("../templates")
    response = client.get("/time")
    assert response.content.decode() == f'''<!DOCTYPE html>
<html>
    <head>
        <title>DevOps lab</title>
    </head>
    <body>
        <h1>Current time in Moscow:{datetime.now(tz=ZoneInfo('Europe/Moscow')).strftime('%H:%M:%S')}</h1>
        <h3>&#x2022; <a href=/>Main page</a> </h3>
    </body>
</html>'''  # noqa: E501
