from typing import Literal

GetAnalyticsLatencyGroupBy = Literal["day", "none"]

GET_ANALYTICS_LATENCY_GROUP_BY_VALUES: set[GetAnalyticsLatencyGroupBy] = {
    "day",
    "none",
}


def check_get_analytics_latency_group_by(value: str) -> GetAnalyticsLatencyGroupBy:
    if value in GET_ANALYTICS_LATENCY_GROUP_BY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_LATENCY_GROUP_BY_VALUES!r}"
    )
