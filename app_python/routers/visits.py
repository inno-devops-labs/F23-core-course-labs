from datetime import datetime, timedelta
from fastapi import APIRouter

from ..schemas.visits import Visits

router = APIRouter(prefix='/api/visits')


@router.get('/get', response_model=Visits)
def get_visits():
    '''Returns number of visits'''
    visits = 0
    with open("/persistence/visits", "r") as f:
        visits = int(f.read())

    return Visits(count=visits)
