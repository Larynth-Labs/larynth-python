from typing import Literal

CallOutcomeGroup = Literal["handled", "needs_look", "not_connected"]

CALL_OUTCOME_GROUP_VALUES: set[CallOutcomeGroup] = {
    "handled",
    "needs_look",
    "not_connected",
}


def check_call_outcome_group(value: str) -> CallOutcomeGroup:
    if value in CALL_OUTCOME_GROUP_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_OUTCOME_GROUP_VALUES!r}"
    )
