from fastapi import APIRouter
import logging

import service
from visits_counter import VisitsCounter


class TimeRouter:
    """

    TimeRouter is a class that specify routes for the service.Timer

    """

    def __init__(self, name: str, route: str, counter: VisitsCounter, logger: logging.Logger):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route(route, self.now, methods=["GET"])

        self.logger = logger
        self.timer = service.Timer(counter, logger)

    async def now(self):
        return self.timer.now()


class VisitsRouter:
    def __init__(self, name: str, route: str, counter: VisitsCounter):
        self.name = name
        self.router = APIRouter()
        self.router.add_api_route(route, self.now, methods=["GET"])

        self.counter = counter

    async def now(self):
        return self.counter.get()