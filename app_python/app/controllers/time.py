"""
Example API implemented using a controller.
"""
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from blacksheep.server.controllers import Controller, get


class TimeController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return ""

    @get()
    async def get_time(self) -> str:
        """
        Gets current time in Moscow.
        """
        time_Moscow = datetime.now(ZoneInfo("Europe/Moscow"))
        time_str = time_Moscow.strftime("%Y-%m-%d %H:%M:%S")
        return "Current time in Moscow: " + time_str
