from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.dnc_entry_scope import DNCEntryScope, check_dnc_entry_scope
from ..models.dnc_entry_source import DNCEntrySource, check_dnc_entry_source
from ..types import UNSET, Unset

T = TypeVar("T", bound="DNCEntry")


@_attrs_define
class DNCEntry:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by (str):
        e164 (str):
        id (UUID):
        scope (DNCEntryScope):
        source (DNCEntrySource):
        call_id (str | Unset):
        category (str | Unset): Opt-out scope; empty covers every call
        reason (str | Unset):
        removed_at (datetime.datetime | Unset):
    """

    created_at: datetime.datetime
    created_by: str
    e164: str
    id: UUID
    scope: DNCEntryScope
    source: DNCEntrySource
    call_id: str | Unset = UNSET
    category: str | Unset = UNSET
    reason: str | Unset = UNSET
    removed_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by = self.created_by

        e164 = self.e164

        id = str(self.id)

        scope: str = self.scope

        source: str = self.source

        call_id = self.call_id

        category = self.category

        reason = self.reason

        removed_at: str | Unset = UNSET
        if not isinstance(self.removed_at, Unset):
            removed_at = self.removed_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "created_by": created_by,
                "e164": e164,
                "id": id,
                "scope": scope,
                "source": source,
            }
        )
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if category is not UNSET:
            field_dict["category"] = category
        if reason is not UNSET:
            field_dict["reason"] = reason
        if removed_at is not UNSET:
            field_dict["removed_at"] = removed_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by = d.pop("created_by")

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        scope = check_dnc_entry_scope(d.pop("scope"))

        source = check_dnc_entry_source(d.pop("source"))

        call_id = d.pop("call_id", UNSET)

        category = d.pop("category", UNSET)

        reason = d.pop("reason", UNSET)

        _removed_at = d.pop("removed_at", UNSET)
        removed_at: datetime.datetime | Unset
        if isinstance(_removed_at, Unset):
            removed_at = UNSET
        else:
            removed_at = datetime.datetime.fromisoformat(_removed_at)

        dnc_entry = cls(
            created_at=created_at,
            created_by=created_by,
            e164=e164,
            id=id,
            scope=scope,
            source=source,
            call_id=call_id,
            category=category,
            reason=reason,
            removed_at=removed_at,
        )

        return dnc_entry
