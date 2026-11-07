from typing import Literal

ListBookingsWhen = Literal["past", "upcoming"]

LIST_BOOKINGS_WHEN_VALUES: set[ListBookingsWhen] = {
    "past",
    "upcoming",
}


def check_list_bookings_when(value: str) -> ListBookingsWhen:
    if value in LIST_BOOKINGS_WHEN_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_BOOKINGS_WHEN_VALUES!r}"
    )
