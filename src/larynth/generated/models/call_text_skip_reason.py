from typing import Literal

CallTextSkipReason = Literal[
    "carrier_not_ready",
    "duplicate",
    "feature_off",
    "no_caller_number",
    "no_consent",
    "opted_out",
    "rate_limited",
    "stop_unclear_hold",
]

CALL_TEXT_SKIP_REASON_VALUES: set[CallTextSkipReason] = {
    "carrier_not_ready",
    "duplicate",
    "feature_off",
    "no_caller_number",
    "no_consent",
    "opted_out",
    "rate_limited",
    "stop_unclear_hold",
}


def check_call_text_skip_reason(value: str) -> CallTextSkipReason:
    if value in CALL_TEXT_SKIP_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TEXT_SKIP_REASON_VALUES!r}"
    )
