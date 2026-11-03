from typing import Literal

CallingRuleSunday = Literal["allowed", "banned", "limited"]

CALLING_RULE_SUNDAY_VALUES: set[CallingRuleSunday] = {
    "allowed",
    "banned",
    "limited",
}


def check_calling_rule_sunday(value: str) -> CallingRuleSunday:
    if value in CALLING_RULE_SUNDAY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALLING_RULE_SUNDAY_VALUES!r}"
    )
