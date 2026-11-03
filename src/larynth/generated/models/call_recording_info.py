from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.call_recording_info_deleted_reason import (
    CallRecordingInfoDeletedReason,
    check_call_recording_info_deleted_reason,
)
from ..models.call_recording_info_state import (
    CallRecordingInfoState,
    check_call_recording_info_state,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CallRecordingInfo")


@_attrs_define
class CallRecordingInfo:
    """
    Attributes:
        id (UUID):
        retention_until (datetime.datetime):
        state (CallRecordingInfoState):
        deleted_at (datetime.datetime | Unset):
        deleted_by_name (str | Unset):
        deleted_reason (CallRecordingInfoDeletedReason | Unset):
    """

    id: UUID
    retention_until: datetime.datetime
    state: CallRecordingInfoState
    deleted_at: datetime.datetime | Unset = UNSET
    deleted_by_name: str | Unset = UNSET
    deleted_reason: CallRecordingInfoDeletedReason | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        retention_until = self.retention_until.isoformat()

        state: str = self.state

        deleted_at: str | Unset = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        deleted_by_name = self.deleted_by_name

        deleted_reason: str | Unset = UNSET
        if not isinstance(self.deleted_reason, Unset):
            deleted_reason = self.deleted_reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "retention_until": retention_until,
                "state": state,
            }
        )
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if deleted_by_name is not UNSET:
            field_dict["deleted_by_name"] = deleted_by_name
        if deleted_reason is not UNSET:
            field_dict["deleted_reason"] = deleted_reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        retention_until = datetime.datetime.fromisoformat(d.pop("retention_until"))

        state = check_call_recording_info_state(d.pop("state"))

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: datetime.datetime | Unset
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = datetime.datetime.fromisoformat(_deleted_at)

        deleted_by_name = d.pop("deleted_by_name", UNSET)

        _deleted_reason = d.pop("deleted_reason", UNSET)
        deleted_reason: CallRecordingInfoDeletedReason | Unset
        if isinstance(_deleted_reason, Unset):
            deleted_reason = UNSET
        else:
            deleted_reason = check_call_recording_info_deleted_reason(_deleted_reason)

        call_recording_info = cls(
            id=id,
            retention_until=retention_until,
            state=state,
            deleted_at=deleted_at,
            deleted_by_name=deleted_by_name,
            deleted_reason=deleted_reason,
        )

        return call_recording_info
