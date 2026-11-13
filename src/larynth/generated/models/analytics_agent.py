from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="AnalyticsAgent")


@_attrs_define
class AnalyticsAgent:
    """
    Attributes:
        assistant_id (UUID):
        avg_duration_ms (int):
        billed_minutes (int):
        booked (int):
        calls (int):
        connected (int):
        name (str):
        p50_latency_ms (int | None): Null when no turn latency was recorded
        spend_micro (int):
    """

    assistant_id: UUID
    avg_duration_ms: int
    billed_minutes: int
    booked: int
    calls: int
    connected: int
    name: str
    p50_latency_ms: int | None
    spend_micro: int

    def to_dict(self) -> dict[str, Any]:
        assistant_id = str(self.assistant_id)

        avg_duration_ms = self.avg_duration_ms

        billed_minutes = self.billed_minutes

        booked = self.booked

        calls = self.calls

        connected = self.connected

        name = self.name

        p50_latency_ms: int | None
        p50_latency_ms = self.p50_latency_ms

        spend_micro = self.spend_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "assistant_id": assistant_id,
                "avg_duration_ms": avg_duration_ms,
                "billed_minutes": billed_minutes,
                "booked": booked,
                "calls": calls,
                "connected": connected,
                "name": name,
                "p50_latency_ms": p50_latency_ms,
                "spend_micro": spend_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        assistant_id = UUID(d.pop("assistant_id"))

        avg_duration_ms = d.pop("avg_duration_ms")

        billed_minutes = d.pop("billed_minutes")

        booked = d.pop("booked")

        calls = d.pop("calls")

        connected = d.pop("connected")

        name = d.pop("name")

        def _parse_p50_latency_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        p50_latency_ms = _parse_p50_latency_ms(d.pop("p50_latency_ms"))

        spend_micro = d.pop("spend_micro")

        analytics_agent = cls(
            assistant_id=assistant_id,
            avg_duration_ms=avg_duration_ms,
            billed_minutes=billed_minutes,
            booked=booked,
            calls=calls,
            connected=connected,
            name=name,
            p50_latency_ms=p50_latency_ms,
            spend_micro=spend_micro,
        )

        return analytics_agent
