from typing import Literal

AlertFiringTrigger = Literal["call_analyzed", "live_turn"]

ALERT_FIRING_TRIGGER_VALUES: set[AlertFiringTrigger] = {
    "call_analyzed",
    "live_turn",
}


def check_alert_firing_trigger(value: str) -> AlertFiringTrigger:
    if value in ALERT_FIRING_TRIGGER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_FIRING_TRIGGER_VALUES!r}"
    )
