from typing import Literal

CallStatus = Literal[
    "busy",
    "canceled",
    "completed",
    "dialing",
    "failed",
    "in_progress",
    "no_answer",
    "queued",
    "rejected",
    "ringing",
]

CALL_STATUS_VALUES: set[CallStatus] = {
    "busy",
    "canceled",
    "completed",
    "dialing",
    "failed",
    "in_progress",
    "no_answer",
    "queued",
    "rejected",
    "ringing",
}


def check_call_status(value: str) -> CallStatus:
    if value in CALL_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_STATUS_VALUES!r}"
    )
