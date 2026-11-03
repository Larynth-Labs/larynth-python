from typing import Literal

GetCallsSummaryBilled = Literal["billed", "not_billed"]

GET_CALLS_SUMMARY_BILLED_VALUES: set[GetCallsSummaryBilled] = {
    "billed",
    "not_billed",
}


def check_get_calls_summary_billed(value: str) -> GetCallsSummaryBilled:
    if value in GET_CALLS_SUMMARY_BILLED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_BILLED_VALUES!r}"
    )
