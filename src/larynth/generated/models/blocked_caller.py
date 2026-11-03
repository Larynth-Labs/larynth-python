from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="BlockedCaller")


@_attrs_define
class BlockedCaller:
    """
    Attributes:
        blocked_calls (int): Calls dropped since the block
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        created_by (UUID | Unset):
        created_by_name (str | Unset):
        last_blocked_at (datetime.datetime | Unset):
        reason (str | Unset):
        source_call_id (str | Unset):
    """

    blocked_calls: int
    created_at: datetime.datetime
    e164: str
    id: UUID
    created_by: UUID | Unset = UNSET
    created_by_name: str | Unset = UNSET
    last_blocked_at: datetime.datetime | Unset = UNSET
    reason: str | Unset = UNSET
    source_call_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        blocked_calls = self.blocked_calls

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        created_by: str | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = str(self.created_by)

        created_by_name = self.created_by_name

        last_blocked_at: str | Unset = UNSET
        if not isinstance(self.last_blocked_at, Unset):
            last_blocked_at = self.last_blocked_at.isoformat()

        reason = self.reason

        source_call_id = self.source_call_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "blocked_calls": blocked_calls,
                "created_at": created_at,
                "e164": e164,
                "id": id,
            }
        )
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if last_blocked_at is not UNSET:
            field_dict["last_blocked_at"] = last_blocked_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if source_call_id is not UNSET:
            field_dict["source_call_id"] = source_call_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        blocked_calls = d.pop("blocked_calls")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        _created_by = d.pop("created_by", UNSET)
        created_by: UUID | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = UUID(_created_by)

        created_by_name = d.pop("created_by_name", UNSET)

        _last_blocked_at = d.pop("last_blocked_at", UNSET)
        last_blocked_at: datetime.datetime | Unset
        if isinstance(_last_blocked_at, Unset):
            last_blocked_at = UNSET
        else:
            last_blocked_at = datetime.datetime.fromisoformat(_last_blocked_at)

        reason = d.pop("reason", UNSET)

        source_call_id = d.pop("source_call_id", UNSET)

        blocked_caller = cls(
            blocked_calls=blocked_calls,
            created_at=created_at,
            e164=e164,
            id=id,
            created_by=created_by,
            created_by_name=created_by_name,
            last_blocked_at=last_blocked_at,
            reason=reason,
            source_call_id=source_call_id,
        )

        return blocked_caller
