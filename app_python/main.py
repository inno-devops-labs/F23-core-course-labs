from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
import logging
import asyncio
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

app = FastAPI()
templates = Jinja2Templates(directory="templates")
counter_lock = asyncio.Lock()

@app.get("/")
async def currentTime(request: Request):

    # Get time in moscow's timezone.
    time_utc = datetime.utcnow()
    time_utc_3 = time_utc + timedelta(hours=3)

    formatted_time = time_utc_3.strftime("%Y-%m-%d %H:%M:%S")
    formatted_request = \
        {"request": request, "current_time": formatted_time}
    async with counter_lock:
        counter_file = open('./data/global_counter.txt', 'r')
        counter = int(counter_file.readline())
        counter += 1
        counter_file = open('./data/global_counter.txt', 'w')
        counter_file.write(f"{counter}")
        counter_file.close()
    return templates.TemplateResponse("currentTime.html", formatted_request)
@app.get("/visits")
async def displayVisits(request: Request):
    async with counter_lock:
        counter_file = open('./data/global_counter.txt', 'r')
        counter = int (counter_file.readline())
        counter += 1
        counter_file = open('./data/global_counter.txt', 'w')
        counter_file.write(f"{counter}")
        counter_file.close()
    formatted_request = \
        {"request": request, "counter": counter}
    return templates.TemplateResponse("visits.html", formatted_request)
# if __name__ == "__main__":
#     # Run the FastAPI app using Uvicorn on port 8080
#     uvicorn.run(app, host="127.0.0.1", port=8080)
