from typing import Literal

SkippedCountReasonCode = Literal[
    "already_enrolled", "dnc", "no_consent", "not_found", "not_us"
]

SKIPPED_COUNT_REASON_CODE_VALUES: set[SkippedCountReasonCode] = {
    "already_enrolled",
    "dnc",
    "no_consent",
    "not_found",
    "not_us",
}


def check_skipped_count_reason_code(value: str) -> SkippedCountReasonCode:
    if value in SKIPPED_COUNT_REASON_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SKIPPED_COUNT_REASON_CODE_VALUES!r}"
    )
