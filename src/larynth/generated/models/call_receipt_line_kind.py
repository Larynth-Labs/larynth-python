from typing import Literal

CallReceiptLineKind = Literal[
    "agent_minutes", "bridged_minutes", "premium_model", "premium_voice"
]

CALL_RECEIPT_LINE_KIND_VALUES: set[CallReceiptLineKind] = {
    "agent_minutes",
    "bridged_minutes",
    "premium_model",
    "premium_voice",
}


def check_call_receipt_line_kind(value: str) -> CallReceiptLineKind:
    if value in CALL_RECEIPT_LINE_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECEIPT_LINE_KIND_VALUES!r}"
    )
