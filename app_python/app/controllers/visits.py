from typing import Optional

from blacksheep.server.controllers import Controller, get


class VisitsController(Controller):
    @classmethod
    def route(cls) -> Optional[str]:
        return "/visits"

    @get()
    async def visits(self) -> str:
        """
        Returns the number of visits to the service from `visits` file.
        """
        with open("visits", "r") as f:
            visits = int(f.read())
        return f"Number of visits: {visits}"
