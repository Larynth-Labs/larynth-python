from typing import Literal

GetAnalyticsLatencyDirection = Literal["inbound", "outbound", "web"]

GET_ANALYTICS_LATENCY_DIRECTION_VALUES: set[GetAnalyticsLatencyDirection] = {
    "inbound",
    "outbound",
    "web",
}


def check_get_analytics_latency_direction(value: str) -> GetAnalyticsLatencyDirection:
    if value in GET_ANALYTICS_LATENCY_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_LATENCY_DIRECTION_VALUES!r}"
    )
