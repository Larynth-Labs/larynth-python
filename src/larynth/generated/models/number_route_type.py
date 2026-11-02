from typing import Literal

NumberRouteType = Literal["assistant", "forward", "none"]

NUMBER_ROUTE_TYPE_VALUES: set[NumberRouteType] = {
    "assistant",
    "forward",
    "none",
}


def check_number_route_type(value: str) -> NumberRouteType:
    if value in NUMBER_ROUTE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NUMBER_ROUTE_TYPE_VALUES!r}"
    )
