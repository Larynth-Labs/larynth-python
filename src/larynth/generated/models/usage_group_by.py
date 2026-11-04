from typing import Literal

UsageGroupBy = Literal["assistant", "category", "day", "number"]

USAGE_GROUP_BY_VALUES: set[UsageGroupBy] = {
    "assistant",
    "category",
    "day",
    "number",
}


def check_usage_group_by(value: str) -> UsageGroupBy:
    if value in USAGE_GROUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USAGE_GROUP_BY_VALUES!r}"
    )
