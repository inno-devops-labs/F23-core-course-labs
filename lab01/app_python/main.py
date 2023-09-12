import fastapi
import uvicorn
import argparse
from datetime import datetime, timezone, timedelta


TIMEZONE_MSK = timezone(timedelta(hours=3))
app = fastapi.FastAPI()


@app.get('/health')
def healthcheck():
    return 'OK'

@app.get('/')
def current_time():
    return datetime.now(tz=TIMEZONE_MSK)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--host',
        type=str,
        default='0.0.0.0',
        help='Interface to listen'
    )
    parser.add_argument('--port', type=int, default=8000, help='Port to listen')
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
