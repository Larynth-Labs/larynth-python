from typing import Literal

FlowEventVia = Literal[
    "ai", "always", "else", "event", "global", "resume", "rule", "start"
]

FLOW_EVENT_VIA_VALUES: set[FlowEventVia] = {
    "ai",
    "always",
    "else",
    "event",
    "global",
    "resume",
    "rule",
    "start",
}


def check_flow_event_via(value: str) -> FlowEventVia:
    if value in FLOW_EVENT_VIA_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FLOW_EVENT_VIA_VALUES!r}"
    )
