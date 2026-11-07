from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BookingService")


@_attrs_define
class BookingService:
    """
    Attributes:
        duration_min (int):
        name (str):
    """

    duration_min: int
    name: str

    def to_dict(self) -> dict[str, Any]:
        duration_min = self.duration_min

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_min": duration_min,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        duration_min = d.pop("duration_min")

        name = d.pop("name")

        booking_service = cls(
            duration_min=duration_min,
            name=name,
        )

        return booking_service
