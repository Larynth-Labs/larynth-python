from typing import Literal

CallOutcomeLabel = Literal["machine", "phone_menu"]

CALL_OUTCOME_LABEL_VALUES: set[CallOutcomeLabel] = {
    "machine",
    "phone_menu",
}


def check_call_outcome_label(value: str) -> CallOutcomeLabel:
    if value in CALL_OUTCOME_LABEL_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_OUTCOME_LABEL_VALUES!r}"
    )
