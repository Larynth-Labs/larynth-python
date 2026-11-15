from typing import Literal

AlertFiringState = Literal["dry_run", "failed", "sent", "throttled"]

ALERT_FIRING_STATE_VALUES: set[AlertFiringState] = {
    "dry_run",
    "failed",
    "sent",
    "throttled",
}


def check_alert_firing_state(value: str) -> AlertFiringState:
    if value in ALERT_FIRING_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ALERT_FIRING_STATE_VALUES!r}"
    )
