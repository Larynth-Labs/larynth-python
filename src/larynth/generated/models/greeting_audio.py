from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GreetingAudio")


@_attrs_define
class GreetingAudio:
    """
    Attributes:
        duration_ms (int):
        sha256 (str): Hex SHA-256 of the stored 16 kHz 16-bit mono PCM
        uploaded_at (datetime.datetime):
    """

    duration_ms: int
    sha256: str
    uploaded_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        duration_ms = self.duration_ms

        sha256 = self.sha256

        uploaded_at = self.uploaded_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_ms": duration_ms,
                "sha256": sha256,
                "uploaded_at": uploaded_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        sha256 = d.pop("sha256")

        uploaded_at = datetime.datetime.fromisoformat(d.pop("uploaded_at"))

        greeting_audio = cls(
            duration_ms=duration_ms,
            sha256=sha256,
            uploaded_at=uploaded_at,
        )

        return greeting_audio
