from fastapi import APIRouter
from datetime import datetime
import pytz

router = APIRouter()

# Define a route for the root URL ("/moscow-time") to obtain the current time in Moscow
@router.get("/moscow-time")
async def get_moscow_time():
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz)
    return {"time": current_time.strftime("%H:%M:%S")}
