from datetime import datetime
from fastapi import Request
from pytz import timezone
import json


def moscow_time():
    time = datetime.now(timezone('Europe/Moscow'))
    return time.strftime("%H:%M:%S")


def get_visits():
    with open('visits.json', 'r') as f:
        visits = json.load(f)

    return {
        'count': len(visits),
        'visits': visits
    }


def record_visit(ip: str):
    with open('visits.json', 'r') as f:
        visits = json.load(f)

    visits.append({
        'ip': ip,
        'time': moscow_time()
    })

    with open('visits.json', 'w') as f:
        json.dump(visits, f, ensure_ascii=False)
        