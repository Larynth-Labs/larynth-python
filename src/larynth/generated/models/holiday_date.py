from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="HolidayDate")


@_attrs_define
class HolidayDate:
    """
    Attributes:
        closed (bool):
        date (datetime.date):
        name (str):
    """

    closed: bool
    date: datetime.date
    name: str

    def to_dict(self) -> dict[str, Any]:
        closed = self.closed

        date = self.date.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "closed": closed,
                "date": date,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        closed = d.pop("closed")

        date = datetime.date.fromisoformat(d.pop("date"))

        name = d.pop("name")

        holiday_date = cls(
            closed=closed,
            date=date,
            name=name,
        )

        return holiday_date
