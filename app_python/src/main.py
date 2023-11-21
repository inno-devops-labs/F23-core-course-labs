from fastapi import FastAPI, Request
from typing import Any, List
from . import utils


app = FastAPI()

@app.get("/")
async def get_current_moscow_time(request: Request):
    utils.record_visit(request.client.host)
    return utils.moscow_time()


@app.get("/visits")
async def get_visits(request: Request):
    utils.record_visit(request.client.host)
    return utils.get_visits()
