from typing import Literal

CallNotBilledReason = Literal["agent_paused", "blocked", "short_call", "spam"]

CALL_NOT_BILLED_REASON_VALUES: set[CallNotBilledReason] = {
    "agent_paused",
    "blocked",
    "short_call",
    "spam",
}


def check_call_not_billed_reason(value: str) -> CallNotBilledReason:
    if value in CALL_NOT_BILLED_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_NOT_BILLED_REASON_VALUES!r}"
    )
