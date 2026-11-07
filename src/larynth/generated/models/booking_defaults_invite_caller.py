from typing import Literal

BookingDefaultsInviteCaller = Literal["off", "optional"]

BOOKING_DEFAULTS_INVITE_CALLER_VALUES: set[BookingDefaultsInviteCaller] = {
    "off",
    "optional",
}


def check_booking_defaults_invite_caller(value: str) -> BookingDefaultsInviteCaller:
    if value in BOOKING_DEFAULTS_INVITE_CALLER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_DEFAULTS_INVITE_CALLER_VALUES!r}"
    )
