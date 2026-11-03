from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.call_transfer_mode import CallTransferMode, check_call_transfer_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallTransfer")


@_attrs_define
class CallTransfer:
    """
    Attributes:
        answered (bool):
        attempts (int):
        destination_name (str):
        mode (CallTransferMode):
        ring_ms (int):
        talk_ms (int):
        leg_call_id (str | Unset):
        started_at (datetime.datetime | Unset):
    """

    answered: bool
    attempts: int
    destination_name: str
    mode: CallTransferMode
    ring_ms: int
    talk_ms: int
    leg_call_id: str | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        answered = self.answered

        attempts = self.attempts

        destination_name = self.destination_name

        mode: str = self.mode

        ring_ms = self.ring_ms

        talk_ms = self.talk_ms

        leg_call_id = self.leg_call_id

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answered": answered,
                "attempts": attempts,
                "destination_name": destination_name,
                "mode": mode,
                "ring_ms": ring_ms,
                "talk_ms": talk_ms,
            }
        )
        if leg_call_id is not UNSET:
            field_dict["leg_call_id"] = leg_call_id
        if started_at is not UNSET:
            field_dict["started_at"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        answered = d.pop("answered")

        attempts = d.pop("attempts")

        destination_name = d.pop("destination_name")

        mode = check_call_transfer_mode(d.pop("mode"))

        ring_ms = d.pop("ring_ms")

        talk_ms = d.pop("talk_ms")

        leg_call_id = d.pop("leg_call_id", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)

        call_transfer = cls(
            answered=answered,
            attempts=attempts,
            destination_name=destination_name,
            mode=mode,
            ring_ms=ring_ms,
            talk_ms=talk_ms,
            leg_call_id=leg_call_id,
            started_at=started_at,
        )

        return call_transfer
