from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from datetime import datetime, timedelta

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def currentTime(request: Request):

    # Get time in moscow's timezone.
    time_utc = datetime.utcnow()
    time_utc_3 = time_utc + timedelta(hours=3)

    formatted_time = time_utc_3.strftime("%Y-%m-%d %H:%M:%S")
    formatted_request = \
        {"request": request, "current_time": formatted_time}
    return templates.TemplateResponse("currentTime.html", formatted_request)


# if __name__ == "__main__":
#     # Run the FastAPI app using Uvicorn on port 8080
#     uvicorn.run(app, host="127.0.0.1", port=8080)
