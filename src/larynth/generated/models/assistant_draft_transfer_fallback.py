from typing import Literal

AssistantDraftTransferFallback = Literal["end", "next_target", "take_message"]

ASSISTANT_DRAFT_TRANSFER_FALLBACK_VALUES: set[AssistantDraftTransferFallback] = {
    "end",
    "next_target",
    "take_message",
}


def check_assistant_draft_transfer_fallback(
    value: str,
) -> AssistantDraftTransferFallback:
    if value in ASSISTANT_DRAFT_TRANSFER_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_DRAFT_TRANSFER_FALLBACK_VALUES!r}"
    )
