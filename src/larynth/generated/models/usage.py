from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.usage_group_by import UsageGroupBy, check_usage_group_by

if TYPE_CHECKING:
    from ..models.usage_row import UsageRow


T = TypeVar("T", bound="Usage")


@_attrs_define
class Usage:
    """
    Attributes:
        from_ (datetime.date):
        group_by (UsageGroupBy):
        ledger_check_micro (int): Charges of the period read straight from the ledger; equals totals.amount_micro
        rows (list[UsageRow]):
        timezone (str):
        to (datetime.date):
        totals (UsageRow):
    """

    from_: datetime.date
    group_by: UsageGroupBy
    ledger_check_micro: int
    rows: list[UsageRow]
    timezone: str
    to: datetime.date
    totals: UsageRow

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.isoformat()

        group_by: str = self.group_by

        ledger_check_micro = self.ledger_check_micro

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        timezone = self.timezone

        to = self.to.isoformat()

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "from": from_,
                "group_by": group_by,
                "ledger_check_micro": ledger_check_micro,
                "rows": rows,
                "timezone": timezone,
                "to": to,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usage_row import UsageRow

        d = dict(src_dict)
        from_ = datetime.date.fromisoformat(d.pop("from"))

        group_by = check_usage_group_by(d.pop("group_by"))

        ledger_check_micro = d.pop("ledger_check_micro")

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = UsageRow.from_dict(rows_item_data)

            rows.append(rows_item)

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        totals = UsageRow.from_dict(d.pop("totals"))

        usage = cls(
            from_=from_,
            group_by=group_by,
            ledger_check_micro=ledger_check_micro,
            rows=rows,
            timezone=timezone,
            to=to,
            totals=totals,
        )

        return usage
