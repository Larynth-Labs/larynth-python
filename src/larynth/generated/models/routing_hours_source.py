from typing import Literal

RoutingHoursSource = Literal["business_profile"]

ROUTING_HOURS_SOURCE_VALUES: set[RoutingHoursSource] = {
    "business_profile",
}


def check_routing_hours_source(value: str) -> RoutingHoursSource:
    if value in ROUTING_HOURS_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTING_HOURS_SOURCE_VALUES!r}"
    )
