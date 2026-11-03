from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CallsSummaryGroup")


@_attrs_define
class CallsSummaryGroup:
    """
    Attributes:
        billed_ms (int):
        booked (int):
        calls (int):
        connected (int):
        key (str): Assistant id, outcome or local date (YYYY-MM-DD)
        spend_micro (int):
    """

    billed_ms: int
    booked: int
    calls: int
    connected: int
    key: str
    spend_micro: int

    def to_dict(self) -> dict[str, Any]:
        billed_ms = self.billed_ms

        booked = self.booked

        calls = self.calls

        connected = self.connected

        key = self.key

        spend_micro = self.spend_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "billed_ms": billed_ms,
                "booked": booked,
                "calls": calls,
                "connected": connected,
                "key": key,
                "spend_micro": spend_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        billed_ms = d.pop("billed_ms")

        booked = d.pop("booked")

        calls = d.pop("calls")

        connected = d.pop("connected")

        key = d.pop("key")

        spend_micro = d.pop("spend_micro")

        calls_summary_group = cls(
            billed_ms=billed_ms,
            booked=booked,
            calls=calls,
            connected=connected,
            key=key,
            spend_micro=spend_micro,
        )

        return calls_summary_group
