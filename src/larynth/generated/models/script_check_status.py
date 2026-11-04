from typing import Literal

ScriptCheckStatus = Literal[
    "approved", "blocked", "flagged", "passed", "pending", "rejected"
]

SCRIPT_CHECK_STATUS_VALUES: set[ScriptCheckStatus] = {
    "approved",
    "blocked",
    "flagged",
    "passed",
    "pending",
    "rejected",
}


def check_script_check_status(value: str) -> ScriptCheckStatus:
    if value in SCRIPT_CHECK_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SCRIPT_CHECK_STATUS_VALUES!r}"
    )
