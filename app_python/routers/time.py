from datetime import datetime, timedelta
from fastapi import APIRouter

from ..schemas.time import NowTime

router = APIRouter(prefix='/api/time')


@router.get('/now', response_model=NowTime)
def get_now():
    '''Returns current time in Moscow'''

    visits = 0
    try:
        with open("/persistence/visits", "r") as f:
            visits = int(f.read())
    except:
        pass
    with open("/persistence/visits", "w") as f:
        f.write(str(visits + 1))

    return NowTime(timestamp=datetime.utcnow() + timedelta(hours=3))
