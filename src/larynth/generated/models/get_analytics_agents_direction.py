from typing import Literal

GetAnalyticsAgentsDirection = Literal["inbound", "outbound", "web"]

GET_ANALYTICS_AGENTS_DIRECTION_VALUES: set[GetAnalyticsAgentsDirection] = {
    "inbound",
    "outbound",
    "web",
}


def check_get_analytics_agents_direction(value: str) -> GetAnalyticsAgentsDirection:
    if value in GET_ANALYTICS_AGENTS_DIRECTION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_ANALYTICS_AGENTS_DIRECTION_VALUES!r}"
    )
