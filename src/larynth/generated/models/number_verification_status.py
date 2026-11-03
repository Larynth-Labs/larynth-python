from typing import Literal

NumberVerificationStatus = Literal["expired", "failed", "verified", "verifying"]

NUMBER_VERIFICATION_STATUS_VALUES: set[NumberVerificationStatus] = {
    "expired",
    "failed",
    "verified",
    "verifying",
}


def check_number_verification_status(value: str) -> NumberVerificationStatus:
    if value in NUMBER_VERIFICATION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_VERIFICATION_STATUS_VALUES!r}"
    )
