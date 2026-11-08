from typing import Literal

BookingHoursSource = Literal["number_routing", "own"]

BOOKING_HOURS_SOURCE_VALUES: set[BookingHoursSource] = {
    "number_routing",
    "own",
}


def check_booking_hours_source(value: str) -> BookingHoursSource:
    if value in BOOKING_HOURS_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BOOKING_HOURS_SOURCE_VALUES!r}"
    )
