from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CallLatency")


@_attrs_define
class CallLatency:
    """
    Attributes:
        avg_ms (int):
        over_target (int): Agent turns slower than the target
        p95_ms (int):
        target_ms (int):
    """

    avg_ms: int
    over_target: int
    p95_ms: int
    target_ms: int

    def to_dict(self) -> dict[str, Any]:
        avg_ms = self.avg_ms

        over_target = self.over_target

        p95_ms = self.p95_ms

        target_ms = self.target_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "avg_ms": avg_ms,
                "over_target": over_target,
                "p95_ms": p95_ms,
                "target_ms": target_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        avg_ms = d.pop("avg_ms")

        over_target = d.pop("over_target")

        p95_ms = d.pop("p95_ms")

        target_ms = d.pop("target_ms")

        call_latency = cls(
            avg_ms=avg_ms,
            over_target=over_target,
            p95_ms=p95_ms,
            target_ms=target_ms,
        )

        return call_latency
