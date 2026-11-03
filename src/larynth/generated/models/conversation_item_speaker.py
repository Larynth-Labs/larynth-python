from typing import Literal

ConversationItemSpeaker = Literal["agent", "caller", "staff", "system"]

CONVERSATION_ITEM_SPEAKER_VALUES: set[ConversationItemSpeaker] = {
    "agent",
    "caller",
    "staff",
    "system",
}


def check_conversation_item_speaker(value: str) -> ConversationItemSpeaker:
    if value in CONVERSATION_ITEM_SPEAKER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_ITEM_SPEAKER_VALUES!r}"
    )
