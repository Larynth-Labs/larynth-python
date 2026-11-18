from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.analytics_usage_day import AnalyticsUsageDay
    from ..models.analytics_usage_split import AnalyticsUsageSplit


T = TypeVar("T", bound="AnalyticsUsage")


@_attrs_define
class AnalyticsUsage:
    """
    Attributes:
        days (list[AnalyticsUsageDay]):
        from_ (datetime.date):
        timezone (str):
        to (datetime.date):
        totals (AnalyticsUsageSplit):
    """

    days: list[AnalyticsUsageDay]
    from_: datetime.date
    timezone: str
    to: datetime.date
    totals: AnalyticsUsageSplit

    def to_dict(self) -> dict[str, Any]:
        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        from_ = self.from_.isoformat()

        timezone = self.timezone

        to = self.to.isoformat()

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "days": days,
                "from": from_,
                "timezone": timezone,
                "to": to,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_usage_day import AnalyticsUsageDay
        from ..models.analytics_usage_split import AnalyticsUsageSplit

        d = dict(src_dict)
        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = AnalyticsUsageDay.from_dict(days_item_data)

            days.append(days_item)

        from_ = datetime.date.fromisoformat(d.pop("from"))

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        totals = AnalyticsUsageSplit.from_dict(d.pop("totals"))

        analytics_usage = cls(
            days=days,
            from_=from_,
            timezone=timezone,
            to=to,
            totals=totals,
        )

        return analytics_usage
