from typing import Literal

PreflightCheckState = Literal["info", "ok", "stop", "warn"]

PREFLIGHT_CHECK_STATE_VALUES: set[PreflightCheckState] = {
    "info",
    "ok",
    "stop",
    "warn",
}


def check_preflight_check_state(value: str) -> PreflightCheckState:
    if value in PREFLIGHT_CHECK_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREFLIGHT_CHECK_STATE_VALUES!r}"
    )
