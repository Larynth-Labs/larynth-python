from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.cost_per_call_row import CostPerCallRow


T = TypeVar("T", bound="CostPerAnsweredCall")


@_attrs_define
class CostPerAnsweredCall:
    """
    Attributes:
        agents (list[CostPerCallRow]): Agents with charges or answered calls, highest charge first; at most 100
        from_ (datetime.date):
        timezone (str):
        to (datetime.date):
        totals (CostPerCallRow):
    """

    agents: list[CostPerCallRow]
    from_: datetime.date
    timezone: str
    to: datetime.date
    totals: CostPerCallRow

    def to_dict(self) -> dict[str, Any]:
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        from_ = self.from_.isoformat()

        timezone = self.timezone

        to = self.to.isoformat()

        totals = self.totals.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agents": agents,
                "from": from_,
                "timezone": timezone,
                "to": to,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cost_per_call_row import CostPerCallRow

        d = dict(src_dict)
        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = CostPerCallRow.from_dict(agents_item_data)

            agents.append(agents_item)

        from_ = datetime.date.fromisoformat(d.pop("from"))

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        totals = CostPerCallRow.from_dict(d.pop("totals"))

        cost_per_answered_call = cls(
            agents=agents,
            from_=from_,
            timezone=timezone,
            to=to,
            totals=totals,
        )

        return cost_per_answered_call
