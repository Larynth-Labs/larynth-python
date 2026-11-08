from typing import Literal

ListBookingsStatusItem = Literal[
    "cancelled",
    "confirmed",
    "declined",
    "failed",
    "held",
    "needs_check",
    "pending_approval",
]

LIST_BOOKINGS_STATUS_ITEM_VALUES: set[ListBookingsStatusItem] = {
    "cancelled",
    "confirmed",
    "declined",
    "failed",
    "held",
    "needs_check",
    "pending_approval",
}


def check_list_bookings_status_item(value: str) -> ListBookingsStatusItem:
    if value in LIST_BOOKINGS_STATUS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_BOOKINGS_STATUS_ITEM_VALUES!r}"
    )
