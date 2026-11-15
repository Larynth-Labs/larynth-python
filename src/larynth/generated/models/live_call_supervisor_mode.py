from typing import Literal

LiveCallSupervisorMode = Literal["listen", "takeover"]

LIVE_CALL_SUPERVISOR_MODE_VALUES: set[LiveCallSupervisorMode] = {
    "listen",
    "takeover",
}


def check_live_call_supervisor_mode(value: str) -> LiveCallSupervisorMode:
    if value in LIVE_CALL_SUPERVISOR_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_SUPERVISOR_MODE_VALUES!r}"
    )
