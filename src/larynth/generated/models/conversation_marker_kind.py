from typing import Literal

ConversationMarkerKind = Literal[
    "disclosure", "dtmf", "opt_out", "recording_notice", "voicemail"
]

CONVERSATION_MARKER_KIND_VALUES: set[ConversationMarkerKind] = {
    "disclosure",
    "dtmf",
    "opt_out",
    "recording_notice",
    "voicemail",
}


def check_conversation_marker_kind(value: str) -> ConversationMarkerKind:
    if value in CONVERSATION_MARKER_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONVERSATION_MARKER_KIND_VALUES!r}"
    )
