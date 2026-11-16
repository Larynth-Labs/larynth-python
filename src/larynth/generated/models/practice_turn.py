from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.practice_turn_speaker import (
    PracticeTurnSpeaker,
    check_practice_turn_speaker,
)

T = TypeVar("T", bound="PracticeTurn")


@_attrs_define
class PracticeTurn:
    """
    Attributes:
        speaker (PracticeTurnSpeaker):
        text (str):
    """

    speaker: PracticeTurnSpeaker
    text: str

    def to_dict(self) -> dict[str, Any]:
        speaker: str = self.speaker

        text = self.text

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "speaker": speaker,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        speaker = check_practice_turn_speaker(d.pop("speaker"))

        text = d.pop("text")

        practice_turn = cls(
            speaker=speaker,
            text=text,
        )

        return practice_turn
