from typing import Literal

BookingDefaultsApproval = Literal["direct", "owner_approval"]

BOOKING_DEFAULTS_APPROVAL_VALUES: set[BookingDefaultsApproval] = {
    "direct",
    "owner_approval",
}


def check_booking_defaults_approval(value: str) -> BookingDefaultsApproval:
    if value in BOOKING_DEFAULTS_APPROVAL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_DEFAULTS_APPROVAL_VALUES!r}"
    )
