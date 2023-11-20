import os
from typing import Awaitable, Callable

from blacksheep import Request, Response


class VisitMiddleware:
    async def __call__(
        self, request: Request, handler: Callable[[Request], Awaitable]
    ) -> Response:
        response = await handler(request)
        # check if folder exists
        if not os.path.exists("data"):
            os.mkdir("data")
        if os.path.exists("data/visits"):
            with open("data/visits", "r") as f:
                visits = int(f.read())
        else:
            visits = 0

        visits += 1

        with open("data/visits", "w") as f:
            f.write(str(visits))

        return response


def configure_middlewares(app):
    app.middlewares.append(VisitMiddleware())
