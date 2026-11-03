from typing import Literal

GetContactTimelineFilter = Literal["all", "calls", "campaigns", "consent"]

GET_CONTACT_TIMELINE_FILTER_VALUES: set[GetContactTimelineFilter] = {
    "all",
    "calls",
    "campaigns",
    "consent",
}


def check_get_contact_timeline_filter(value: str) -> GetContactTimelineFilter:
    if value in GET_CONTACT_TIMELINE_FILTER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CONTACT_TIMELINE_FILTER_VALUES!r}"
    )
