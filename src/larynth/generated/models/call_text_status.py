from typing import Literal

CallTextStatus = Literal["failed", "queued", "received", "sent", "skipped"]

CALL_TEXT_STATUS_VALUES: set[CallTextStatus] = {
    "failed",
    "queued",
    "received",
    "sent",
    "skipped",
}


def check_call_text_status(value: str) -> CallTextStatus:
    if value in CALL_TEXT_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TEXT_STATUS_VALUES!r}"
    )
