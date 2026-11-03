from typing import Literal

ScheduleSummaryKey = Literal["around_the_clock", "weekly"]

SCHEDULE_SUMMARY_KEY_VALUES: set[ScheduleSummaryKey] = {
    "around_the_clock",
    "weekly",
}


def check_schedule_summary_key(value: str) -> ScheduleSummaryKey:
    if value in SCHEDULE_SUMMARY_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCHEDULE_SUMMARY_KEY_VALUES!r}"
    )
