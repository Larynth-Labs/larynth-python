from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HolidayCalendarDate")


@_attrs_define
class HolidayCalendarDate:
    """
    Attributes:
        date (datetime.date):
        name (str):
    """

    date: datetime.date
    name: str

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        name = d.pop("name")

        holiday_calendar_date = cls(
            date=date,
            name=name,
        )

        return holiday_calendar_date
