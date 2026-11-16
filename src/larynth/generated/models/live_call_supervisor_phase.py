from typing import Literal

LiveCallSupervisorPhase = Literal[
    "awaiting_key",
    "briefing",
    "handing_back",
    "joined",
    "joining",
    "listening",
    "requested",
    "ringing",
    "screening",
]

LIVE_CALL_SUPERVISOR_PHASE_VALUES: set[LiveCallSupervisorPhase] = {
    "awaiting_key",
    "briefing",
    "handing_back",
    "joined",
    "joining",
    "listening",
    "requested",
    "ringing",
    "screening",
}


def check_live_call_supervisor_phase(value: str) -> LiveCallSupervisorPhase:
    if value in LIVE_CALL_SUPERVISOR_PHASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIVE_CALL_SUPERVISOR_PHASE_VALUES!r}"
    )
