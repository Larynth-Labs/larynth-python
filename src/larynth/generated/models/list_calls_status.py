from typing import Literal

ListCallsStatus = Literal[
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

LIST_CALLS_STATUS_VALUES: set[ListCallsStatus] = {
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


def check_list_calls_status(value: str) -> ListCallsStatus:
    if value in LIST_CALLS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_STATUS_VALUES!r}"
    )
