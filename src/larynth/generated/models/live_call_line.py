from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.live_call_line_speaker import (
    LiveCallLineSpeaker,
    check_live_call_line_speaker,
)

T = TypeVar("T", bound="LiveCallLine")


@_attrs_define
class LiveCallLine:
    """
    Attributes:
        at (datetime.datetime):
        speaker (LiveCallLineSpeaker):
        text (str):
    """

    at: datetime.datetime
    speaker: LiveCallLineSpeaker
    text: str

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        speaker: str = self.speaker

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "speaker": speaker,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        speaker = check_live_call_line_speaker(d.pop("speaker"))

        text = d.pop("text")

        live_call_line = cls(
            at=at,
            speaker=speaker,
            text=text,
        )

        return live_call_line
