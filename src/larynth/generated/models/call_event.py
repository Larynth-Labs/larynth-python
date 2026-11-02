from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.call_event_kind import CallEventKind, check_call_event_kind

if TYPE_CHECKING:
    from ..models.call_event_payload import CallEventPayload


T = TypeVar("T", bound="CallEvent")


@_attrs_define
class CallEvent:
    """
    Attributes:
        at (datetime.datetime):
        event_id (str):
        kind (CallEventKind):
        payload (CallEventPayload): protojson of the engine CallEvent payload
        seq (int):
    """

    at: datetime.datetime
    event_id: str
    kind: CallEventKind
    payload: CallEventPayload
    seq: int

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        event_id = self.event_id

        kind: str = self.kind

        payload = self.payload.to_dict()

        seq = self.seq

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "event_id": event_id,
                "kind": kind,
                "payload": payload,
                "seq": seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_event_payload import CallEventPayload

        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        event_id = d.pop("event_id")

        kind = check_call_event_kind(d.pop("kind"))

        payload = CallEventPayload.from_dict(d.pop("payload"))

        seq = d.pop("seq")

        call_event = cls(
            at=at,
            event_id=event_id,
            kind=kind,
            payload=payload,
            seq=seq,
        )

        return call_event
