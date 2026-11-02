from typing import Literal

NumberRoutingRouteType = Literal["assistant", "forward", "none"]

NUMBER_ROUTING_ROUTE_TYPE_VALUES: set[NumberRoutingRouteType] = {
    "assistant",
    "forward",
    "none",
}


def check_number_routing_route_type(value: str) -> NumberRoutingRouteType:
    if value in NUMBER_ROUTING_ROUTE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_ROUTING_ROUTE_TYPE_VALUES!r}"
    )
