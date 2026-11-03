from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.holiday_settings import HolidaySettings
    from ..models.hours_band import HoursBand


T = TypeVar("T", bound="RoutingHours")


@_attrs_define
class RoutingHours:
    """
    Attributes:
        bands (list[HoursBand]): At most 2 bands per day, no overlaps
        holidays (HolidaySettings):
        timezone (str): IANA zone; defaults to the workspace time zone
    """

    bands: list[HoursBand]
    holidays: HolidaySettings
    timezone: str

    def to_dict(self) -> dict[str, Any]:
        bands = []
        for bands_item_data in self.bands:
            bands_item = bands_item_data.to_dict()
            bands.append(bands_item)

        holidays = self.holidays.to_dict()

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bands": bands,
                "holidays": holidays,
                "timezone": timezone,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.holiday_settings import HolidaySettings
        from ..models.hours_band import HoursBand

        d = dict(src_dict)
        bands = []
        _bands = d.pop("bands")
        for bands_item_data in _bands:
            bands_item = HoursBand.from_dict(bands_item_data)

            bands.append(bands_item)

        holidays = HolidaySettings.from_dict(d.pop("holidays"))

        timezone = d.pop("timezone")

        routing_hours = cls(
            bands=bands,
            holidays=holidays,
            timezone=timezone,
        )

        return routing_hours
