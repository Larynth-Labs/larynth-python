from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AssistantCoverageBand")


@_attrs_define
class AssistantCoverageBand:
    """
    Attributes:
        days (list[str]): mon to sun
        end_minute (int):
        start_minute (int):
    """

    days: list[str]
    end_minute: int
    start_minute: int

    def to_dict(self) -> dict[str, Any]:
        days = self.days

        end_minute = self.end_minute

        start_minute = self.start_minute

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "days": days,
                "end_minute": end_minute,
                "start_minute": start_minute,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        days = cast(list[str], d.pop("days"))

        end_minute = d.pop("end_minute")

        start_minute = d.pop("start_minute")

        assistant_coverage_band = cls(
            days=days,
            end_minute=end_minute,
            start_minute=start_minute,
        )

        return assistant_coverage_band
