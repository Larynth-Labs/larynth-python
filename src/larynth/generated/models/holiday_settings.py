from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.holiday_settings_calendar import (
    HolidaySettingsCalendar,
    check_holiday_settings_calendar,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.holiday_date import HolidayDate


T = TypeVar("T", bound="HolidaySettings")


@_attrs_define
class HolidaySettings:
    """
    Attributes:
        dates (list[HolidayDate]): Own dates within the next 24 months
        calendar (HolidaySettingsCalendar | Unset): Preset calendar; empty for none
    """

    dates: list[HolidayDate]
    calendar: HolidaySettingsCalendar | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.to_dict()
            dates.append(dates_item)

        calendar: str | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dates": dates,
            }
        )
        if calendar is not UNSET:
            field_dict["calendar"] = calendar

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.holiday_date import HolidayDate

        d = dict(src_dict)
        dates = []
        _dates = d.pop("dates")
        for dates_item_data in _dates:
            dates_item = HolidayDate.from_dict(dates_item_data)

            dates.append(dates_item)

        _calendar = d.pop("calendar", UNSET)
        calendar: HolidaySettingsCalendar | Unset
        if isinstance(_calendar, Unset):
            calendar = UNSET
        else:
            calendar = check_holiday_settings_calendar(_calendar)

        holiday_settings = cls(
            dates=dates,
            calendar=calendar,
        )

        return holiday_settings
