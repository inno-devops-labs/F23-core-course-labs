from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from pytz import timezone

app = FastAPI()
Instrumentator().instrument(app).expose(app)


def get_visits(path: str):
    path = Path(path)
    if not path.exists() or path.stat().st_size == 0:
        return 0
    with open(path, "r") as f:
        return int(f.read())


def update_visits(path: str, visits: int):
    visits += 1
    with open(path, "w") as f:
        f.write(str(visits))
    return visits


@app.get("/")
def time_endpoint():
    moscow = timezone("Europe/Moscow")
    moscow_time = datetime.now(moscow)
    return {"time": moscow_time.strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/visits")
def visits_endpoint():
    path = "data/visits"
    visits = get_visits(path)
    visits = update_visits(path, visits)
    return {"visits": visits}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
