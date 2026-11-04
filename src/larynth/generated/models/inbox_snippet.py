from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.inbox_snippet_speaker import (
    InboxSnippetSpeaker,
    check_inbox_snippet_speaker,
)

T = TypeVar("T", bound="InboxSnippet")


@_attrs_define
class InboxSnippet:
    """
    Attributes:
        at_ms (int):
        speaker (InboxSnippetSpeaker):
        text (str):
    """

    at_ms: int
    speaker: InboxSnippetSpeaker
    text: str

    def to_dict(self) -> dict[str, Any]:
        at_ms = self.at_ms

        speaker: str = self.speaker

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at_ms": at_ms,
                "speaker": speaker,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at_ms = d.pop("at_ms")

        speaker = check_inbox_snippet_speaker(d.pop("speaker"))

        text = d.pop("text")

        inbox_snippet = cls(
            at_ms=at_ms,
            speaker=speaker,
            text=text,
        )

        return inbox_snippet
