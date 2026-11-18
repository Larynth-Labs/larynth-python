from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_text_direction import CallTextDirection, check_call_text_direction
from ..models.call_text_kind import CallTextKind, check_call_text_kind
from ..models.call_text_skip_reason import (
    CallTextSkipReason,
    check_call_text_skip_reason,
)
from ..models.call_text_status import CallTextStatus, check_call_text_status
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallText")


@_attrs_define
class CallText:
    """
    Attributes:
        body (None | str): null after the retention period or a caller erasure
        created_at (datetime.datetime):
        direction (CallTextDirection):
        id (UUID):
        kind (CallTextKind):
        status (CallTextStatus):
        error (str | Unset): Carrier failure class, for example rejected or not_enabled
        sent_at (datetime.datetime | Unset):
        skip_reason (CallTextSkipReason | Unset):
        template_key (str | Unset):
    """

    body: None | str
    created_at: datetime.datetime
    direction: CallTextDirection
    id: UUID
    kind: CallTextKind
    status: CallTextStatus
    error: str | Unset = UNSET
    sent_at: datetime.datetime | Unset = UNSET
    skip_reason: CallTextSkipReason | Unset = UNSET
    template_key: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        body: None | str
        body = self.body

        created_at = self.created_at.isoformat()

        direction: str = self.direction

        id = str(self.id)

        kind: str = self.kind

        status: str = self.status

        error = self.error

        sent_at: str | Unset = UNSET
        if not isinstance(self.sent_at, Unset):
            sent_at = self.sent_at.isoformat()

        skip_reason: str | Unset = UNSET
        if not isinstance(self.skip_reason, Unset):
            skip_reason = self.skip_reason

        template_key = self.template_key

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "body": body,
                "created_at": created_at,
                "direction": direction,
                "id": id,
                "kind": kind,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if sent_at is not UNSET:
            field_dict["sent_at"] = sent_at
        if skip_reason is not UNSET:
            field_dict["skip_reason"] = skip_reason
        if template_key is not UNSET:
            field_dict["template_key"] = template_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)

        def _parse_body(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        body = _parse_body(d.pop("body"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        direction = check_call_text_direction(d.pop("direction"))

        id = UUID(d.pop("id"))

        kind = check_call_text_kind(d.pop("kind"))

        status = check_call_text_status(d.pop("status"))

        error = d.pop("error", UNSET)

        _sent_at = d.pop("sent_at", UNSET)
        sent_at: datetime.datetime | Unset
        if isinstance(_sent_at, Unset):
            sent_at = UNSET
        else:
            sent_at = datetime.datetime.fromisoformat(_sent_at)

        _skip_reason = d.pop("skip_reason", UNSET)
        skip_reason: CallTextSkipReason | Unset
        if isinstance(_skip_reason, Unset):
            skip_reason = UNSET
        else:
            skip_reason = check_call_text_skip_reason(_skip_reason)

        template_key = d.pop("template_key", UNSET)

        call_text = cls(
            body=body,
            created_at=created_at,
            direction=direction,
            id=id,
            kind=kind,
            status=status,
            error=error,
            sent_at=sent_at,
            skip_reason=skip_reason,
            template_key=template_key,
        )

        return call_text
