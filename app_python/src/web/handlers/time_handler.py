from aiohttp import web
from typing import Type
from datetime import datetime

from .abstract import WebHandler
from src.domain.time_tracker import UTCTimeTracker


class TimeWebHandler(WebHandler):
    def __init__(self, time_tracker: Type[UTCTimeTracker], shift_delta: int):

        self._time_tracker = time_tracker(time_shift_delta=shift_delta)
        self._time_format = "%Y-%m-%d %H:%M:%S:%f"

        try:
            with open("./volume/calls.db", 'r') as file:
                self.calls = int(file.read())
        except FileNotFoundError:
            self.calls = 0


        super().__init__()

    def _add_handlers(self):
        self._routers.append(web.get('/', self.get_time))
        self._routers.append(web.get('/visits', self.get_calls))

    async def _get_formatted_time(self, time: datetime) -> str:
        return time.strftime(self._time_format)

    async def get_time(self, request) -> web.Response:
        self.calls += 1
        with open("./volume/calls.db", 'w') as file:
            print(self.calls, file=file)
        time: str = await self._get_formatted_time(self._time_tracker.get_timezoned_current_time())
        return web.Response(text=f'{time}')

    async def get_calls(self, request) -> web.Response:
        return web.Response(text="{ \"calls\": " + f"{self.calls}" + "}")
