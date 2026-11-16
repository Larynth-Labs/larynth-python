from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.analytics_agent_latency import AnalyticsAgentLatency
    from ..models.analytics_latency_day import AnalyticsLatencyDay


T = TypeVar("T", bound="AnalyticsLatency")


@_attrs_define
class AnalyticsLatency:
    """
    Attributes:
        agents (list[AnalyticsAgentLatency]):
        days (list[AnalyticsLatencyDay]):
        from_ (datetime.date):
        p50_ms (int | None): Caller finished to agent heard; null when no turn latency was recorded
        p95_ms (int | None):
        timezone (str):
        to (datetime.date):
        turns (int):
    """

    agents: list[AnalyticsAgentLatency]
    days: list[AnalyticsLatencyDay]
    from_: datetime.date
    p50_ms: int | None
    p95_ms: int | None
    timezone: str
    to: datetime.date
    turns: int

    def to_dict(self) -> dict[str, Any]:
        agents = []
        for agents_item_data in self.agents:
            agents_item = agents_item_data.to_dict()
            agents.append(agents_item)

        days = []
        for days_item_data in self.days:
            days_item = days_item_data.to_dict()
            days.append(days_item)

        from_ = self.from_.isoformat()

        p50_ms: int | None
        p50_ms = self.p50_ms

        p95_ms: int | None
        p95_ms = self.p95_ms

        timezone = self.timezone

        to = self.to.isoformat()

        turns = self.turns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agents": agents,
                "days": days,
                "from": from_,
                "p50_ms": p50_ms,
                "p95_ms": p95_ms,
                "timezone": timezone,
                "to": to,
                "turns": turns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_agent_latency import AnalyticsAgentLatency
        from ..models.analytics_latency_day import AnalyticsLatencyDay

        d = dict(src_dict)
        agents = []
        _agents = d.pop("agents")
        for agents_item_data in _agents:
            agents_item = AnalyticsAgentLatency.from_dict(agents_item_data)

            agents.append(agents_item)

        days = []
        _days = d.pop("days")
        for days_item_data in _days:
            days_item = AnalyticsLatencyDay.from_dict(days_item_data)

            days.append(days_item)

        from_ = datetime.date.fromisoformat(d.pop("from"))

        def _parse_p50_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        p50_ms = _parse_p50_ms(d.pop("p50_ms"))

        def _parse_p95_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        p95_ms = _parse_p95_ms(d.pop("p95_ms"))

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        turns = d.pop("turns")

        analytics_latency = cls(
            agents=agents,
            days=days,
            from_=from_,
            p50_ms=p50_ms,
            p95_ms=p95_ms,
            timezone=timezone,
            to=to,
            turns=turns,
        )

        return analytics_latency
