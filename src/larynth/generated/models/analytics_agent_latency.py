from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsAgentLatency")


@_attrs_define
class AnalyticsAgentLatency:
    """
    Attributes:
        assistant_id (UUID):
        name (str):
        p50_ms (int | None):
        p95_ms (int | None):
        turns (int):
    """

    assistant_id: UUID
    name: str
    p50_ms: int | None
    p95_ms: int | None
    turns: int

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        name = self.name

        p50_ms: int | None
        p50_ms = self.p50_ms

        p95_ms: int | None
        p95_ms = self.p95_ms

        turns = self.turns

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "name": name,
                "p50_ms": p50_ms,
                "p95_ms": p95_ms,
                "turns": turns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        name = d.pop("name")

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

        analytics_agent_latency = cls(
            assistant_id=assistant_id,
            name=name,
            p50_ms=p50_ms,
            p95_ms=p95_ms,
            turns=turns,
        )

        return analytics_agent_latency
