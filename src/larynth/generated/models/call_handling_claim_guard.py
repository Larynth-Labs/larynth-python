from typing import Literal

CallHandlingClaimGuard = Literal["count", "off", "rewrite"]

CALL_HANDLING_CLAIM_GUARD_VALUES: set[CallHandlingClaimGuard] = {
    "count",
    "off",
    "rewrite",
}


def check_call_handling_claim_guard(value: str) -> CallHandlingClaimGuard:
    if value in CALL_HANDLING_CLAIM_GUARD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_HANDLING_CLAIM_GUARD_VALUES!r}"
    )
