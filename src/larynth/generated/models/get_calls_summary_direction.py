from typing import Literal

GetCallsSummaryDirection = Literal["inbound", "outbound", "web_test"]

GET_CALLS_SUMMARY_DIRECTION_VALUES: set[GetCallsSummaryDirection] = {
    "inbound",
    "outbound",
    "web_test",
}


def check_get_calls_summary_direction(value: str) -> GetCallsSummaryDirection:
    if value in GET_CALLS_SUMMARY_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_DIRECTION_VALUES!r}"
    )
