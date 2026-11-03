from typing import Literal

GetCallingRulesPurpose = Literal["informational", "telemarketing"]

GET_CALLING_RULES_PURPOSE_VALUES: set[GetCallingRulesPurpose] = {
    "informational",
    "telemarketing",
}


def check_get_calling_rules_purpose(value: str) -> GetCallingRulesPurpose:
    if value in GET_CALLING_RULES_PURPOSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_CALLING_RULES_PURPOSE_VALUES!r}"
    )
