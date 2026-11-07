from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MonthlyStatement")


@_attrs_define
class MonthlyStatement:
    """
    Attributes:
        complete (bool): False for the current month (statement so far)
        from_ (datetime.date):
        month (str):
        to (datetime.date):
    """

    complete: bool
    from_: datetime.date
    month: str
    to: datetime.date

    def to_dict(self) -> dict[str, Any]:
        complete = self.complete

        from_ = self.from_.isoformat()

        month = self.month

        to = self.to.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "complete": complete,
                "from": from_,
                "month": month,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        complete = d.pop("complete")

        from_ = datetime.date.fromisoformat(d.pop("from"))

        month = d.pop("month")

        to = datetime.date.fromisoformat(d.pop("to"))

        monthly_statement = cls(
            complete=complete,
            from_=from_,
            month=month,
            to=to,
        )

        return monthly_statement
