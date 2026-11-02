from typing import Literal

CallHangupBy = Literal["local", "remote", "system"]

CALL_HANGUP_BY_VALUES: set[CallHangupBy] = {
    "local",
    "remote",
    "system",
}


def check_call_hangup_by(value: str) -> CallHangupBy:
    if value in CALL_HANGUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANGUP_BY_VALUES!r}"
    )
