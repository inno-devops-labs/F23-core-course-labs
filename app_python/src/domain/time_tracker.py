from datetime import datetime, timedelta, timezone

MOSCOW_TIMEZONE_SHIFT = 3


class UTCTimeTracker:
    def __init__(self, time_shift_delta: int) -> None:
        self.time_shift_delta = time_shift_delta
        self.time_zone = timezone(timedelta(hours=self.time_shift_delta), name="MSC")

    def get_timezoned_current_time(self) -> datetime:
        return datetime.now().astimezone(self.time_zone)

    def get_iso_format(self, mask="") -> str:
        if mask:
            return self.get_timezoned_current_time().strftime(mask)
        return self.get_timezoned_current_time().isoformat()

    def __str__(self) -> str:
        return str(self.get_timezoned_current_time())


utc_time_mocsow_tracker = UTCTimeTracker(MOSCOW_TIMEZONE_SHIFT)
