from typing import Literal

GetAnalyticsUsageGroupBy = Literal["day", "none"]

GET_ANALYTICS_USAGE_GROUP_BY_VALUES: set[GetAnalyticsUsageGroupBy] = {
    "day",
    "none",
}


def check_get_analytics_usage_group_by(value: str) -> GetAnalyticsUsageGroupBy:
    if value in GET_ANALYTICS_USAGE_GROUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_USAGE_GROUP_BY_VALUES!r}"
    )
