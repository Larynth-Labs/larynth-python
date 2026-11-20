from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_recording_lane_lane import (
    CallRecordingLaneLane,
    check_call_recording_lane_lane,
)

T = TypeVar("T", bound="CallRecordingLane")


@_attrs_define
class CallRecordingLane:
    """
    Attributes:
        lane (CallRecordingLaneLane):
        points (list[float]): Normalised 0 to 1 per lane; every lane has the same count on the same timeline
        recording_id (UUID):
    """

    lane: CallRecordingLaneLane
    points: list[float]
    recording_id: UUID

    def to_dict(self) -> dict[str, Any]:
        lane: str = self.lane

        points = self.points

        recording_id = str(self.recording_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "lane": lane,
                "points": points,
                "recording_id": recording_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        lane = check_call_recording_lane_lane(d.pop("lane"))

        points = cast(list[float], d.pop("points"))

        recording_id = UUID(d.pop("recording_id"))

        call_recording_lane = cls(
            lane=lane,
            points=points,
            recording_id=recording_id,
        )

        return call_recording_lane
