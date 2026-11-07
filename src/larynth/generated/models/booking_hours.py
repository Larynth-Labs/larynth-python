from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.booking_hours_source import BookingHoursSource, check_booking_hours_source
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hours_band import HoursBand


T = TypeVar("T", bound="BookingHours")


@_attrs_define
class BookingHours:
    """
    Attributes:
        source (BookingHoursSource): number_routing uses the business hours of the number the call came in on
        bands (list[HoursBand] | Unset): own only; the W2 routing hours bands
        timezone (str | Unset): IANA zone; own only
    """

    source: BookingHoursSource
    bands: list[HoursBand] | Unset = UNSET
    timezone: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        source: str = self.source

        bands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bands, Unset):
            bands = []
            for bands_item_data in self.bands:
                bands_item = bands_item_data.to_dict()
                bands.append(bands_item)

        timezone = self.timezone

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
            }
        )
        if bands is not UNSET:
            field_dict["bands"] = bands
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.hours_band import HoursBand

        d = dict(src_dict)
        source = check_booking_hours_source(d.pop("source"))

        _bands = d.pop("bands", UNSET)
        bands: list[HoursBand] | Unset = UNSET
        if _bands is not UNSET:
            bands = []
            for bands_item_data in _bands:
                bands_item = HoursBand.from_dict(bands_item_data)

                bands.append(bands_item)

        timezone = d.pop("timezone", UNSET)

        booking_hours = cls(
            source=source,
            bands=bands,
            timezone=timezone,
        )

        return booking_hours
