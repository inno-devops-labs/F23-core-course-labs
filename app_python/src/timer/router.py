import time

from fastapi import FastAPI, APIRouter

from .service import Timer


class TimeRouter:

    """

    TimeRouter is a class that specify routes for the service.Timer

    """

    def __init__(self, name: str, route: str):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route(route, self.now, methods=["GET"])

        self.timer = Timer()

    async def now(self):
        return self.timer.now()
