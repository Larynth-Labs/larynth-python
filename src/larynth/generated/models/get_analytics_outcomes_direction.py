from typing import Literal

GetAnalyticsOutcomesDirection = Literal["inbound", "outbound", "web"]

GET_ANALYTICS_OUTCOMES_DIRECTION_VALUES: set[GetAnalyticsOutcomesDirection] = {
    "inbound",
    "outbound",
    "web",
}


def check_get_analytics_outcomes_direction(value: str) -> GetAnalyticsOutcomesDirection:
    if value in GET_ANALYTICS_OUTCOMES_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_OUTCOMES_DIRECTION_VALUES!r}"
    )
