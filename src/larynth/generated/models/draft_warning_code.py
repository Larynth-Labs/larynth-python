from typing import Literal

DraftWarningCode = Literal[
    "knowledge_not_ready",
    "language_not_switchable",
    "unknown_variable",
    "voice_language_mismatch",
]

DRAFT_WARNING_CODE_VALUES: set[DraftWarningCode] = {
    "knowledge_not_ready",
    "language_not_switchable",
    "unknown_variable",
    "voice_language_mismatch",
}


def check_draft_warning_code(value: str) -> DraftWarningCode:
    if value in DRAFT_WARNING_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DRAFT_WARNING_CODE_VALUES!r}"
    )
