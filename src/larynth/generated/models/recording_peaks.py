from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="RecordingPeaks")


@_attrs_define
class RecordingPeaks:
    """
    Attributes:
        duration_ms (int):
        points (list[float]): Normalised 0 to 1
    """

    duration_ms: int
    points: list[float]

    def to_dict(self) -> dict[str, Any]:
        duration_ms = self.duration_ms

        points = self.points

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_ms": duration_ms,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        points = cast(list[float], d.pop("points"))

        recording_peaks = cls(
            duration_ms=duration_ms,
            points=points,
        )

        return recording_peaks
