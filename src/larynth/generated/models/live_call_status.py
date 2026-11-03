from typing import Literal

LiveCallStatus = Literal["dialing", "in_progress", "queued", "ringing"]

LIVE_CALL_STATUS_VALUES: set[LiveCallStatus] = {
    "dialing",
    "in_progress",
    "queued",
    "ringing",
}


def check_live_call_status(value: str) -> LiveCallStatus:
    if value in LIVE_CALL_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_STATUS_VALUES!r}"
    )
