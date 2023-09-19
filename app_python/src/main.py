"""
This is a FastAPI application that returns
the current date and time in the "Europe/Moscow" timezone.
"""

from zoneinfo import ZoneInfo
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_main():
    """
    Get the current date and time in the "Europe/Moscow" timezone and return it as a message.

    Returns:
        str: A greeting message along with the current date and time.
    """
    current_time = datetime.now(tz=ZoneInfo(
                    "Europe/Moscow")).strftime("%d/%m/%Y %H:%M:%S")
    return f"Hello, User! The date and time: {current_time}"
