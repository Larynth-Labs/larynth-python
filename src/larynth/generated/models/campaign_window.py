from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="CampaignWindow")


@_attrs_define
class CampaignWindow:
    """
    Attributes:
        days (list[int]): 0 = Sunday … 6 = Saturday, callee local time
        end_minute (int):
        start_minute (int):
    """

    days: list[int]
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
        days = cast(list[int], d.pop("days"))

        end_minute = d.pop("end_minute")

        start_minute = d.pop("start_minute")

        campaign_window = cls(
            days=days,
            end_minute=end_minute,
            start_minute=start_minute,
        )

        return campaign_window
