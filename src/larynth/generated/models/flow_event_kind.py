from typing import Literal

FlowEventKind = Literal["ended", "guard_tripped", "node_entered", "variable_set"]

FLOW_EVENT_KIND_VALUES: set[FlowEventKind] = {
    "ended",
    "guard_tripped",
    "node_entered",
    "variable_set",
}


def check_flow_event_kind(value: str) -> FlowEventKind:
    if value in FLOW_EVENT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FLOW_EVENT_KIND_VALUES!r}"
    )
