from typing import Literal

BookingStatus = Literal[
    "cancelled",
    "confirmed",
    "declined",
    "failed",
    "held",
    "needs_check",
    "pending_approval",
]

BOOKING_STATUS_VALUES: set[BookingStatus] = {
    "cancelled",
    "confirmed",
    "declined",
    "failed",
    "held",
    "needs_check",
    "pending_approval",
}


def check_booking_status(value: str) -> BookingStatus:
    if value in BOOKING_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_STATUS_VALUES!r}"
    )
