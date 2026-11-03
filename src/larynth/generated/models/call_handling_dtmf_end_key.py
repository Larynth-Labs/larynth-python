from typing import Literal

CallHandlingDtmfEndKey = Literal["#", "*", "none"]

CALL_HANDLING_DTMF_END_KEY_VALUES: set[CallHandlingDtmfEndKey] = {
    "#",
    "*",
    "none",
}


def check_call_handling_dtmf_end_key(value: str) -> CallHandlingDtmfEndKey:
    if value in CALL_HANDLING_DTMF_END_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_DTMF_END_KEY_VALUES!r}"
    )
