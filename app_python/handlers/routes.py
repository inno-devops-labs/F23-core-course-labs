from app_python.config import config
from datetime import datetime
from flask import request, Response
from flask import current_app
from pathlib import Path
from prometheus_client import Summary, generate_latest
from io import TextIOWrapper
import os.path

visits_count: int = 0

def configure_visits(app):
    global visits_count
    try:
        vists_path = Path(config["VISITS_PATH"])
        vists_path.parent.mkdir(exist_ok=True, parents=True)
        vists_path.touch(exist_ok=True)
        
        if os.path.getsize(vists_path) > 0:
            with open(vists_path) as f:
                visits_count = int(str(f.read()))

    except Exception as e:
        app.logger.error(f"Failed to read app visits from file: {e}")

def increment_visits():
    global visits_count
    visits_count += 1
    
    with open(config["VISITS_PATH"], "w") as f:
        f.write(str(visits_count))

def configure_routes(app):
    global visits_count

    request_duration = Summary('http_request_duration_seconds', 'HTTP request duration in seconds')
    

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    @request_duration.time()
    # Displays current time in the timezone configured by the
    # TZ configuration variable according to the format from
    # the FORMAT configuration variable
    def display_time(path):
        increment_visits()
        
        now = datetime.now(tz=config["TZ"])
        time = now.strftime(config["FORMAT"])

        ip: str = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)   
        app.logger.info(f'Showing time {time} to {ip}')
        return time
    
    @app.route('/metrics')
    def metrics():
        CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

    configure_visits(app)

    @app.route('/visits')
    def visits():
        global visits_count
        return str(visits_count)
