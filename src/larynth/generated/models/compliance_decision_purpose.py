from typing import Literal

ComplianceDecisionPurpose = Literal["informational", "telemarketing"]

COMPLIANCE_DECISION_PURPOSE_VALUES: set[ComplianceDecisionPurpose] = {
    "informational",
    "telemarketing",
}


def check_compliance_decision_purpose(value: str) -> ComplianceDecisionPurpose:
    if value in COMPLIANCE_DECISION_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_DECISION_PURPOSE_VALUES!r}"
    )
