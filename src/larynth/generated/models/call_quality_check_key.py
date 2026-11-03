from typing import Literal

CallQualityCheckKey = Literal[
    "accurate_answers",
    "ended_cleanly",
    "followed_guardrails",
    "greeting",
    "handled_next_step",
    "reply_speed",
    "stayed_on_task",
    "understood_caller",
]

CALL_QUALITY_CHECK_KEY_VALUES: set[CallQualityCheckKey] = {
    "accurate_answers",
    "ended_cleanly",
    "followed_guardrails",
    "greeting",
    "handled_next_step",
    "reply_speed",
    "stayed_on_task",
    "understood_caller",
}


def check_call_quality_check_key(value: str) -> CallQualityCheckKey:
    if value in CALL_QUALITY_CHECK_KEY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_QUALITY_CHECK_KEY_VALUES!r}"
    )
