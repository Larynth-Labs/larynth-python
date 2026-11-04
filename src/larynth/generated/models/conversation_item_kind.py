from typing import Literal

ConversationItemKind = Literal["marker", "tool", "transfer", "turn"]

CONVERSATION_ITEM_KIND_VALUES: set[ConversationItemKind] = {
    "marker",
    "tool",
    "transfer",
    "turn",
}


def check_conversation_item_kind(value: str) -> ConversationItemKind:
    if value in CONVERSATION_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_ITEM_KIND_VALUES!r}"
    )
