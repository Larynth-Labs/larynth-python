from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.analytics_agent import AnalyticsAgent


T = TypeVar("T", bound="AnalyticsAgents")


@_attrs_define
class AnalyticsAgents:
    """
    Attributes:
        data (list[AnalyticsAgent]):
        from_ (datetime.date):
        timezone (str):
        to (datetime.date):
    """

    data: list[AnalyticsAgent]
    from_: datetime.date
    timezone: str
    to: datetime.date

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        from_ = self.from_.isoformat()

        timezone = self.timezone

        to = self.to.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "from": from_,
                "timezone": timezone,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_agent import AnalyticsAgent

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = AnalyticsAgent.from_dict(data_item_data)

            data.append(data_item)

        from_ = datetime.date.fromisoformat(d.pop("from"))

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        analytics_agents = cls(
            data=data,
            from_=from_,
            timezone=timezone,
            to=to,
        )

        return analytics_agents
