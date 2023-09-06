from datetime import datetime, timedelta
from fastapi import APIRouter

from ..schemas.time import NowTime

router = APIRouter(prefix='/api/time')

@router.get('/now', response_model=NowTime)
def get_now():
    '''Returns current time in Moscow'''
    return NowTime(timestamp=datetime.utcnow() + timedelta(hours=3))
