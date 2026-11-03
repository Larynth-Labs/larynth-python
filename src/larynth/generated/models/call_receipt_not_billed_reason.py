from typing import Literal

CallReceiptNotBilledReason = Literal["agent_paused", "blocked", "short_call", "spam"]

CALL_RECEIPT_NOT_BILLED_REASON_VALUES: set[CallReceiptNotBilledReason] = {
    "agent_paused",
    "blocked",
    "short_call",
    "spam",
}


def check_call_receipt_not_billed_reason(value: str) -> CallReceiptNotBilledReason:
    if value in CALL_RECEIPT_NOT_BILLED_REASON_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CALL_RECEIPT_NOT_BILLED_REASON_VALUES!r}"
    )
