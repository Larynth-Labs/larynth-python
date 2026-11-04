from typing import Literal

TimelineCallDirection = Literal["inbound", "outbound", "web_test"]

TIMELINE_CALL_DIRECTION_VALUES: set[TimelineCallDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_timeline_call_direction(value: str) -> TimelineCallDirection:
    if value in TIMELINE_CALL_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TIMELINE_CALL_DIRECTION_VALUES!r}"
    )
