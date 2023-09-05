import api.service.time as time_service


class Time():
    def __init__(self) -> None:
        self.timezone = 'Europe/Moscow'
        self.time = time_service.current_formatted_time(self.timezone)
