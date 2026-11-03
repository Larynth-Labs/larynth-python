from typing import Literal

AssistantVersionSpecTransferFallback = Literal["end", "next_target", "take_message"]

ASSISTANT_VERSION_SPEC_TRANSFER_FALLBACK_VALUES: set[
    AssistantVersionSpecTransferFallback
] = {
    "end",
    "next_target",
    "take_message",
}


def check_assistant_version_spec_transfer_fallback(
    value: str,
) -> AssistantVersionSpecTransferFallback:
    if value in ASSISTANT_VERSION_SPEC_TRANSFER_FALLBACK_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_VERSION_SPEC_TRANSFER_FALLBACK_VALUES!r}"
    )
