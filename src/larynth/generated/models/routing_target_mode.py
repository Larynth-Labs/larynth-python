from typing import Literal

RoutingTargetMode = Literal["assistant", "forward"]

ROUTING_TARGET_MODE_VALUES: set[RoutingTargetMode] = {
    "assistant",
    "forward",
}


def check_routing_target_mode(value: str) -> RoutingTargetMode:
    if value in ROUTING_TARGET_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ROUTING_TARGET_MODE_VALUES!r}"
    )
