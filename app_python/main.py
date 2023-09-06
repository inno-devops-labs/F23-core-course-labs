from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def currentTime(request: Request):

    # Get time in moscow's timezone.
    time_utc = datetime.utcnow()
    time_utc_3 = time_utc + timedelta(hours=3)

    formatted_time = time_utc_3.strftime("%Y-%m-%d %H:%M:%S")

    return templates.TemplateResponse("currentTime.html", {"request": request, "current_time": formatted_time})


# if __name__ == "__main__":
#     # Run the FastAPI app using Uvicorn on port 8000
#     uvicorn.run(app, host="0.0.0.0", port=8000)
