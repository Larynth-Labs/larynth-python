from typing import Literal

FlowValidationIssueSeverity = Literal["error", "warning"]

FLOW_VALIDATION_ISSUE_SEVERITY_VALUES: set[FlowValidationIssueSeverity] = {
    "error",
    "warning",
}


def check_flow_validation_issue_severity(value: str) -> FlowValidationIssueSeverity:
    if value in FLOW_VALIDATION_ISSUE_SEVERITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FLOW_VALIDATION_ISSUE_SEVERITY_VALUES!r}"
    )
