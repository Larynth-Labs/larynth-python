from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.call_recording_lane import CallRecordingLane


T = TypeVar("T", bound="CallRecordingPeaks")


@_attrs_define
class CallRecordingPeaks:
    """
    Attributes:
        duration_ms (int):
        lanes (list[CallRecordingLane]):
    """

    duration_ms: int
    lanes: list[CallRecordingLane]

    def to_dict(self) -> dict[str, Any]:
        duration_ms = self.duration_ms

        lanes = []
        for lanes_item_data in self.lanes:
            lanes_item = lanes_item_data.to_dict()
            lanes.append(lanes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_ms": duration_ms,
                "lanes": lanes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_recording_lane import CallRecordingLane

        d = dict(src_dict)
        duration_ms = d.pop("duration_ms")

        lanes = []
        _lanes = d.pop("lanes")
        for lanes_item_data in _lanes:
            lanes_item = CallRecordingLane.from_dict(lanes_item_data)

            lanes.append(lanes_item)

        call_recording_peaks = cls(
            duration_ms=duration_ms,
            lanes=lanes,
        )

        return call_recording_peaks
