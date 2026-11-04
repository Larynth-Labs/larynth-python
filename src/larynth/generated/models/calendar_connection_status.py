from typing import Literal

CalendarConnectionStatus = Literal["connected", "needs_reconnect", "revoked"]

CALENDAR_CONNECTION_STATUS_VALUES: set[CalendarConnectionStatus] = {
    "connected",
    "needs_reconnect",
    "revoked",
}


def check_calendar_connection_status(value: str) -> CalendarConnectionStatus:
    if value in CALENDAR_CONNECTION_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_CONNECTION_STATUS_VALUES!r}"
    )
