from typing import Literal

CompareSectionKey = Literal[
    "advanced",
    "basics",
    "call_handling",
    "disclosures",
    "guardrails",
    "instructions",
    "knowledge",
    "model",
    "post_call",
    "tools",
    "voice",
]

COMPARE_SECTION_KEY_VALUES: set[CompareSectionKey] = {
    "advanced",
    "basics",
    "call_handling",
    "disclosures",
    "guardrails",
    "instructions",
    "knowledge",
    "model",
    "post_call",
    "tools",
    "voice",
}


def check_compare_section_key(value: str) -> CompareSectionKey:
    if value in COMPARE_SECTION_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPARE_SECTION_KEY_VALUES!r}"
    )
