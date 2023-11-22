from os import environ, path
import pytz
from logging.config import dictConfig

config = {
    'TZ': pytz.timezone(environ.get("CLOCK_TZ", "Europe/Moscow")),
    'HOST': environ.get("HOST", "0.0.0.0"),
    'FORMAT': "%Y-%m-%d %H:%M:%S",
    'VISITS_PATH': environ.get("VISITS_PATH", "/app_python/data/visits.txt")
} 


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(module)s [%(levelname)s] : %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})