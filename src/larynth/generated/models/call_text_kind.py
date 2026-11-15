from typing import Literal

CallTextKind = Literal[
    "help",
    "reply",
    "start",
    "stop",
    "stop_clarify",
    "stop_confirm",
    "template",
    "unclear",
]

CALL_TEXT_KIND_VALUES: set[CallTextKind] = {
    "help",
    "reply",
    "start",
    "stop",
    "stop_clarify",
    "stop_confirm",
    "template",
    "unclear",
}


def check_call_text_kind(value: str) -> CallTextKind:
    if value in CALL_TEXT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_TEXT_KIND_VALUES!r}"
    )
