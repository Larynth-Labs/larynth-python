from typing import Literal

CallHandlingMaxReply = Literal["long", "normal", "short"]

CALL_HANDLING_MAX_REPLY_VALUES: set[CallHandlingMaxReply] = {
    "long",
    "normal",
    "short",
}


def check_call_handling_max_reply(value: str) -> CallHandlingMaxReply:
    if value in CALL_HANDLING_MAX_REPLY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_MAX_REPLY_VALUES!r}"
    )
