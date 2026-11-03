from typing import Literal

ListCallsOrder = Literal[
    "-duration", "-price", "-started", "duration", "price", "started"
]

LIST_CALLS_ORDER_VALUES: set[ListCallsOrder] = {
    "-duration",
    "-price",
    "-started",
    "duration",
    "price",
    "started",
}


def check_list_calls_order(value: str) -> ListCallsOrder:
    if value in LIST_CALLS_ORDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_ORDER_VALUES!r}"
    )
