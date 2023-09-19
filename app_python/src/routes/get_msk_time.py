from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from pydantic import BaseModel
import pytz
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

class TimeZoneRequest(BaseModel):
    timezone: str = "Europe/Moscow"

# Define a route for the root URL ("/moscow-time") to obtain the current time in Moscow
@router.get("/time")
async def get_time(request_data: TimeZoneRequest = Depends()):
    try:
        tz = pytz.timezone(request_data.timezone)
        current_time = datetime.now(tz)
        logger.info(f"{request_data.timezone} time retrieved successfully")
        return {"time": current_time.strftime("%H:%M:%S")}
    except pytz.exceptions.UnknownTimeZoneError:
        logger.error(f"Invalid timezone provided: {request_data.timezone}")
        raise HTTPException(status_code=400, detail="Invalid timezone provided")
