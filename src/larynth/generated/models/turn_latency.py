from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="TurnLatency")


@_attrs_define
class TurnLatency:
    """
    Attributes:
        eot_ms (int): Caller finished
        llm_ms (int): Thought
        over_target (bool):
        stt_ms (int): Heard
        total_ms (int): Caller finished to agent heard
        tts_ms (int): Voice
    """

    eot_ms: int
    llm_ms: int
    over_target: bool
    stt_ms: int
    total_ms: int
    tts_ms: int

    def to_dict(self) -> dict[str, Any]:
        eot_ms = self.eot_ms

        llm_ms = self.llm_ms

        over_target = self.over_target

        stt_ms = self.stt_ms

        total_ms = self.total_ms

        tts_ms = self.tts_ms

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "eot_ms": eot_ms,
                "llm_ms": llm_ms,
                "over_target": over_target,
                "stt_ms": stt_ms,
                "total_ms": total_ms,
                "tts_ms": tts_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        eot_ms = d.pop("eot_ms")

        llm_ms = d.pop("llm_ms")

        over_target = d.pop("over_target")

        stt_ms = d.pop("stt_ms")

        total_ms = d.pop("total_ms")

        tts_ms = d.pop("tts_ms")

        turn_latency = cls(
            eot_ms=eot_ms,
            llm_ms=llm_ms,
            over_target=over_target,
            stt_ms=stt_ms,
            total_ms=total_ms,
            tts_ms=tts_ms,
        )

        return turn_latency
