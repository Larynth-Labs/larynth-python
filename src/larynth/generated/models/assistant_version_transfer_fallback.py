from typing import Literal

AssistantVersionTransferFallback = Literal["end", "next_target", "take_message"]

ASSISTANT_VERSION_TRANSFER_FALLBACK_VALUES: set[AssistantVersionTransferFallback] = {
    "end",
    "next_target",
    "take_message",
}


def check_assistant_version_transfer_fallback(
    value: str,
) -> AssistantVersionTransferFallback:
    if value in ASSISTANT_VERSION_TRANSFER_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_TRANSFER_FALLBACK_VALUES!r}"
    )
