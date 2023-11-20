import os
from typing import Awaitable, Callable

from blacksheep import Request, Response


class VisitMiddleware:
    async def __call__(
        self, request: Request, handler: Callable[[Request], Awaitable]
    ) -> Response:
        response = await handler(request)

        if os.path.exists("visits"):
            with open("visits", "r") as f:
                visits = int(f.read())
        else:
            visits = 0

        visits += 1

        with open("visits", "w") as f:
            f.write(str(visits))

        return response


def configure_middlewares(app):
    app.middlewares.append(VisitMiddleware())
