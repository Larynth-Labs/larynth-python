from typing import Literal

GetCallsSummaryStatus = Literal[
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

GET_CALLS_SUMMARY_STATUS_VALUES: set[GetCallsSummaryStatus] = {
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


def check_get_calls_summary_status(value: str) -> GetCallsSummaryStatus:
    if value in GET_CALLS_SUMMARY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_STATUS_VALUES!r}"
    )
