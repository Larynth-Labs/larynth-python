from typing import Literal

ListCallsDirection = Literal["inbound", "outbound", "web_test"]

LIST_CALLS_DIRECTION_VALUES: set[ListCallsDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_list_calls_direction(value: str) -> ListCallsDirection:
    if value in LIST_CALLS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CALLS_DIRECTION_VALUES!r}"
    )
