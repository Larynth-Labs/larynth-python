from typing import Literal

GuardrailBuiltInCategory = Literal[
    "compliance", "honesty", "privacy", "safety", "scope"
]

GUARDRAIL_BUILT_IN_CATEGORY_VALUES: set[GuardrailBuiltInCategory] = {
    "compliance",
    "honesty",
    "privacy",
    "safety",
    "scope",
}


def check_guardrail_built_in_category(value: str) -> GuardrailBuiltInCategory:
    if value in GUARDRAIL_BUILT_IN_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GUARDRAIL_BUILT_IN_CATEGORY_VALUES!r}"
    )
