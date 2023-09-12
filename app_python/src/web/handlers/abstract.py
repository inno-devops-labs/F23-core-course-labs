from abc import ABC, abstractmethod


class WebHandler(ABC):
    def __init__(self, **kwargs):
        self._routers: list = []

        self._add_handlers()

    @abstractmethod
    def _add_handlers(self):
        ...

    def get_routers(self) -> list:
        return self._routers
