from typing import Optional

from blacksheep.server.controllers import Controller, get


class TimeController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/health"

    @get()
    async def healthcheck(self) -> str:
        """
        Healthcheck endpoint.
        """
        return "OK"
