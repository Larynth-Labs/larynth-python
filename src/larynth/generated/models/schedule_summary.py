from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.schedule_summary_key import ScheduleSummaryKey, check_schedule_summary_key
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hours_band import HoursBand


T = TypeVar("T", bound="ScheduleSummary")


@_attrs_define
class ScheduleSummary:
    """
    Attributes:
        bands (list[HoursBand]):
        key (ScheduleSummaryKey):
        timezone (str | Unset):
    """

    bands: list[HoursBand]
    key: ScheduleSummaryKey
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bands = []
        for bands_item_data in self.bands:
            bands_item = bands_item_data.to_dict()
            bands.append(bands_item)

        key: str = self.key

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bands": bands,
                "key": key,
            }
        )
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hours_band import HoursBand

        d = dict(src_dict)
        bands = []
        _bands = d.pop("bands")
        for bands_item_data in _bands:
            bands_item = HoursBand.from_dict(bands_item_data)

            bands.append(bands_item)

        key = check_schedule_summary_key(d.pop("key"))

        timezone = d.pop("timezone", UNSET)

        schedule_summary = cls(
            bands=bands,
            key=key,
            timezone=timezone,
        )

        return schedule_summary
