from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.holiday_calendar import HolidayCalendar


T = TypeVar("T", bound="ListHolidayCalendar")


@_attrs_define
class ListHolidayCalendar:
    """
    Attributes:
        data (list[HolidayCalendar]):
    """

    data: list[HolidayCalendar]

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.holiday_calendar import HolidayCalendar

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = HolidayCalendar.from_dict(data_item_data)

            data.append(data_item)

        list_holiday_calendar = cls(
            data=data,
        )

        return list_holiday_calendar
