from typing import Literal

CallUnbackedClaimReason = Literal["no_record", "no_tool", "tool_failed"]

CALL_UNBACKED_CLAIM_REASON_VALUES: set[CallUnbackedClaimReason] = {
    "no_record",
    "no_tool",
    "tool_failed",
}


def check_call_unbacked_claim_reason(value: str) -> CallUnbackedClaimReason:
    if value in CALL_UNBACKED_CLAIM_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_UNBACKED_CLAIM_REASON_VALUES!r}"
    )
