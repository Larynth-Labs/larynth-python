from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="VoiceRef")


@_attrs_define
class VoiceRef:
    """
    Attributes:
        provider_key (str):
        voice_key (str):
    """

    provider_key: str
    voice_key: str

    def to_dict(self) -> dict[str, Any]:
        provider_key = self.provider_key

        voice_key = self.voice_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider_key": provider_key,
                "voice_key": voice_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        provider_key = d.pop("provider_key")

        voice_key = d.pop("voice_key")

        voice_ref = cls(
            provider_key=provider_key,
            voice_key=voice_key,
        )

        return voice_ref
