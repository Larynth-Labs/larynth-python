from typing import Literal

GetAnalyticsUsageDirection = Literal["inbound", "outbound", "web"]

GET_ANALYTICS_USAGE_DIRECTION_VALUES: set[GetAnalyticsUsageDirection] = {
    "inbound",
    "outbound",
    "web",
}


def check_get_analytics_usage_direction(value: str) -> GetAnalyticsUsageDirection:
    if value in GET_ANALYTICS_USAGE_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_USAGE_DIRECTION_VALUES!r}"
    )
