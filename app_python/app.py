from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get('/api/time')
def show_time():
    """
    Get current time in Moscow in '%Y-%m-%d %H:%M:%S format.

    ### Output:
    * **Current time in Moscow**: time in '%Y-%m-%d %H:%M:%S' format
    """
    moscow_tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return {"Current time in Moscow": current_time}
