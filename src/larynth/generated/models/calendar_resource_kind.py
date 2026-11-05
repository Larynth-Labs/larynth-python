from typing import Literal

CalendarResourceKind = Literal["calendar", "event_type"]

CALENDAR_RESOURCE_KIND_VALUES: set[CalendarResourceKind] = {
    "calendar",
    "event_type",
}


def check_calendar_resource_kind(value: str) -> CalendarResourceKind:
    if value in CALENDAR_RESOURCE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALENDAR_RESOURCE_KIND_VALUES!r}"
    )
