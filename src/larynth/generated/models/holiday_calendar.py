from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.holiday_calendar_key import HolidayCalendarKey, check_holiday_calendar_key

if TYPE_CHECKING:
    from ..models.holiday_calendar_date import HolidayCalendarDate


T = TypeVar("T", bound="HolidayCalendar")


@_attrs_define
class HolidayCalendar:
    """
    Attributes:
        dates (list[HolidayCalendarDate]):
        key (HolidayCalendarKey):
        name (str):
    """

    dates: list[HolidayCalendarDate]
    key: HolidayCalendarKey
    name: str

    def to_dict(self) -> dict[str, Any]:
        dates = []
        for dates_item_data in self.dates:
            dates_item = dates_item_data.to_dict()
            dates.append(dates_item)

        key: str = self.key

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "dates": dates,
                "key": key,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.holiday_calendar_date import HolidayCalendarDate

        d = dict(src_dict)
        dates = []
        _dates = d.pop("dates")
        for dates_item_data in _dates:
            dates_item = HolidayCalendarDate.from_dict(dates_item_data)

            dates.append(dates_item)

        key = check_holiday_calendar_key(d.pop("key"))

        name = d.pop("name")

        holiday_calendar = cls(
            dates=dates,
            key=key,
            name=name,
        )

        return holiday_calendar
