from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsLatencyDay")


@_attrs_define
class AnalyticsLatencyDay:
    """
    Attributes:
        date (datetime.date):
        p50_ms (int | None): Null on days without recorded turn latency
        p95_ms (int | None):
        turns (int):
    """

    date: datetime.date
    p50_ms: int | None
    p95_ms: int | None
    turns: int

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        p50_ms: int | None
        p50_ms = self.p50_ms

        p95_ms: int | None
        p95_ms = self.p95_ms

        turns = self.turns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "date": date,
                "p50_ms": p50_ms,
                "p95_ms": p95_ms,
                "turns": turns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

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

        turns = d.pop("turns")

        analytics_latency_day = cls(
            date=date,
            p50_ms=p50_ms,
            p95_ms=p95_ms,
            turns=turns,
        )

        return analytics_latency_day
