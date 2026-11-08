from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.calendar_connection import CalendarConnection


T = TypeVar("T", bound="ListCalendarConnection")


@_attrs_define
class ListCalendarConnection:
    """
    Attributes:
        data (list[CalendarConnection]):
    """

    data: list[CalendarConnection]

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
        from ..models.calendar_connection import CalendarConnection

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = CalendarConnection.from_dict(data_item_data)

            data.append(data_item)

        list_calendar_connection = cls(
            data=data,
        )

        return list_calendar_connection
