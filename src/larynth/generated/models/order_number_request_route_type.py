from typing import Literal

OrderNumberRequestRouteType = Literal["assistant", "forward", "none"]

ORDER_NUMBER_REQUEST_ROUTE_TYPE_VALUES: set[OrderNumberRequestRouteType] = {
    "assistant",
    "forward",
    "none",
}


def check_order_number_request_route_type(value: str) -> OrderNumberRequestRouteType:
    if value in ORDER_NUMBER_REQUEST_ROUTE_TYPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORDER_NUMBER_REQUEST_ROUTE_TYPE_VALUES!r}"
    )
