from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.routing_hours_source import RoutingHoursSource, check_routing_hours_source
from ..types import UNSET, Unset

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
        source (RoutingHoursSource | Unset): business_profile: use the workspace business profile's weekly and special
            hours; bands are the fallback while the profile has no weekly hours
    """

    bands: list[HoursBand]
    holidays: HolidaySettings
    timezone: str
    source: RoutingHoursSource | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bands = []
        for bands_item_data in self.bands:
            bands_item = bands_item_data.to_dict()
            bands.append(bands_item)

        holidays = self.holidays.to_dict()

        timezone = self.timezone

        source: str | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bands": bands,
                "holidays": holidays,
                "timezone": timezone,
            }
        )
        if source is not UNSET:
            field_dict["source"] = source

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

        _source = d.pop("source", UNSET)
        source: RoutingHoursSource | Unset
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = check_routing_hours_source(_source)

        routing_hours = cls(
            bands=bands,
            holidays=holidays,
            timezone=timezone,
            source=source,
        )

        return routing_hours
