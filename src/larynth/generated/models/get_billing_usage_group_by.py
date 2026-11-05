from typing import Literal

GetBillingUsageGroupBy = Literal["assistant", "category", "day", "number"]

GET_BILLING_USAGE_GROUP_BY_VALUES: set[GetBillingUsageGroupBy] = {
    "assistant",
    "category",
    "day",
    "number",
}


def check_get_billing_usage_group_by(value: str) -> GetBillingUsageGroupBy:
    if value in GET_BILLING_USAGE_GROUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_BILLING_USAGE_GROUP_BY_VALUES!r}"
    )
