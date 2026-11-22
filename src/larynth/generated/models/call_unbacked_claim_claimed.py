from typing import Literal

CallUnbackedClaimClaimed = Literal[
    "booked", "cancelled", "saved", "scheduled", "sent", "transferred"
]

CALL_UNBACKED_CLAIM_CLAIMED_VALUES: set[CallUnbackedClaimClaimed] = {
    "booked",
    "cancelled",
    "saved",
    "scheduled",
    "sent",
    "transferred",
}


def check_call_unbacked_claim_claimed(value: str) -> CallUnbackedClaimClaimed:
    if value in CALL_UNBACKED_CLAIM_CLAIMED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_UNBACKED_CLAIM_CLAIMED_VALUES!r}"
    )
