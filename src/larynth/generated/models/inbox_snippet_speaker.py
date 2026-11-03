from typing import Literal

InboxSnippetSpeaker = Literal["agent", "caller", "staff"]

INBOX_SNIPPET_SPEAKER_VALUES: set[InboxSnippetSpeaker] = {
    "agent",
    "caller",
    "staff",
}


def check_inbox_snippet_speaker(value: str) -> InboxSnippetSpeaker:
    if value in INBOX_SNIPPET_SPEAKER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INBOX_SNIPPET_SPEAKER_VALUES!r}"
    )
