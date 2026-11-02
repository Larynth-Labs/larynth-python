from typing import Literal

ListComplianceDecisionsResult = Literal["allow", "deny"]

LIST_COMPLIANCE_DECISIONS_RESULT_VALUES: set[ListComplianceDecisionsResult] = {
    "allow",
    "deny",
}


def check_list_compliance_decisions_result(value: str) -> ListComplianceDecisionsResult:
    if value in LIST_COMPLIANCE_DECISIONS_RESULT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_COMPLIANCE_DECISIONS_RESULT_VALUES!r}"
    )
