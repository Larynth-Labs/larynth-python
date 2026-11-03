from typing import Literal

GetCallsSummaryGroupBy = Literal["assistant", "day", "none", "number", "outcome"]

GET_CALLS_SUMMARY_GROUP_BY_VALUES: set[GetCallsSummaryGroupBy] = {
    "assistant",
    "day",
    "none",
    "number",
    "outcome",
}


def check_get_calls_summary_group_by(value: str) -> GetCallsSummaryGroupBy:
    if value in GET_CALLS_SUMMARY_GROUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLS_SUMMARY_GROUP_BY_VALUES!r}"
    )
