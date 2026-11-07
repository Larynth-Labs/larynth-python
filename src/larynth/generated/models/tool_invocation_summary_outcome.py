from typing import Literal

ToolInvocationSummaryOutcome = Literal[
    "blocked", "canceled", "circuit_open", "error", "ok", "timeout"
]

TOOL_INVOCATION_SUMMARY_OUTCOME_VALUES: set[ToolInvocationSummaryOutcome] = {
    "blocked",
    "canceled",
    "circuit_open",
    "error",
    "ok",
    "timeout",
}


def check_tool_invocation_summary_outcome(value: str) -> ToolInvocationSummaryOutcome:
    if value in TOOL_INVOCATION_SUMMARY_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TOOL_INVOCATION_SUMMARY_OUTCOME_VALUES!r}"
    )
