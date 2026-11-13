from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.analytics_outcome_count import AnalyticsOutcomeCount


T = TypeVar("T", bound="AnalyticsOutcomes")


@_attrs_define
class AnalyticsOutcomes:
    """
    Attributes:
        avg_duration_ms (int): Answered to ended, over calls that have both
        calls (int):
        connected (int):
        from_ (datetime.date):
        opted_out (int):
        outcomes (list[AnalyticsOutcomeCount]):
        timezone (str):
        to (datetime.date):
    """

    avg_duration_ms: int
    calls: int
    connected: int
    from_: datetime.date
    opted_out: int
    outcomes: list[AnalyticsOutcomeCount]
    timezone: str
    to: datetime.date

    def to_dict(self) -> dict[str, Any]:
        avg_duration_ms = self.avg_duration_ms

        calls = self.calls

        connected = self.connected

        from_ = self.from_.isoformat()

        opted_out = self.opted_out

        outcomes = []
        for outcomes_item_data in self.outcomes:
            outcomes_item = outcomes_item_data.to_dict()
            outcomes.append(outcomes_item)

        timezone = self.timezone

        to = self.to.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg_duration_ms": avg_duration_ms,
                "calls": calls,
                "connected": connected,
                "from": from_,
                "opted_out": opted_out,
                "outcomes": outcomes,
                "timezone": timezone,
                "to": to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.analytics_outcome_count import AnalyticsOutcomeCount

        d = dict(src_dict)
        avg_duration_ms = d.pop("avg_duration_ms")

        calls = d.pop("calls")

        connected = d.pop("connected")

        from_ = datetime.date.fromisoformat(d.pop("from"))

        opted_out = d.pop("opted_out")

        outcomes = []
        _outcomes = d.pop("outcomes")
        for outcomes_item_data in _outcomes:
            outcomes_item = AnalyticsOutcomeCount.from_dict(outcomes_item_data)

            outcomes.append(outcomes_item)

        timezone = d.pop("timezone")

        to = datetime.date.fromisoformat(d.pop("to"))

        analytics_outcomes = cls(
            avg_duration_ms=avg_duration_ms,
            calls=calls,
            connected=connected,
            from_=from_,
            opted_out=opted_out,
            outcomes=outcomes,
            timezone=timezone,
            to=to,
        )

        return analytics_outcomes
