from typing import Literal

CallEventKind = Literal[
    "amd",
    "answered",
    "compliance",
    "ended",
    "handoff",
    "recording",
    "started",
    "tool",
    "transcript",
    "turn",
]

CALL_EVENT_KIND_VALUES: set[CallEventKind] = {
    "amd",
    "answered",
    "compliance",
    "ended",
    "handoff",
    "recording",
    "started",
    "tool",
    "transcript",
    "turn",
}


def check_call_event_kind(value: str) -> CallEventKind:
    if value in CALL_EVENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_EVENT_KIND_VALUES!r}"
    )
