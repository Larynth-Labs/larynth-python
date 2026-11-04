from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.revocation_channel import RevocationChannel, check_revocation_channel
from ..types import UNSET, Unset

T = TypeVar("T", bound="Revocation")


@_attrs_define
class Revocation:
    """
    Attributes:
        channel (RevocationChannel):
        complaint (bool):
        created_at (datetime.datetime):
        e164 (str):
        id (UUID):
        recorded_by (str):
        revoked_at (datetime.datetime):
        call_id (str | Unset):
        category (str | Unset): Opt-out scope; empty covers every call
        excerpt (str | Unset):
    """

    channel: RevocationChannel
    complaint: bool
    created_at: datetime.datetime
    e164: str
    id: UUID
    recorded_by: str
    revoked_at: datetime.datetime
    call_id: str | Unset = UNSET
    category: str | Unset = UNSET
    excerpt: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel: str = self.channel

        complaint = self.complaint

        created_at = self.created_at.isoformat()

        e164 = self.e164

        id = str(self.id)

        recorded_by = self.recorded_by

        revoked_at = self.revoked_at.isoformat()

        call_id = self.call_id

        category = self.category

        excerpt = self.excerpt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channel": channel,
                "complaint": complaint,
                "created_at": created_at,
                "e164": e164,
                "id": id,
                "recorded_by": recorded_by,
                "revoked_at": revoked_at,
            }
        )
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if category is not UNSET:
            field_dict["category"] = category
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = check_revocation_channel(d.pop("channel"))

        complaint = d.pop("complaint")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        e164 = d.pop("e164")

        id = UUID(d.pop("id"))

        recorded_by = d.pop("recorded_by")

        revoked_at = datetime.datetime.fromisoformat(d.pop("revoked_at"))

        call_id = d.pop("call_id", UNSET)

        category = d.pop("category", UNSET)

        excerpt = d.pop("excerpt", UNSET)

        revocation = cls(
            channel=channel,
            complaint=complaint,
            created_at=created_at,
            e164=e164,
            id=id,
            recorded_by=recorded_by,
            revoked_at=revoked_at,
            call_id=call_id,
            category=category,
            excerpt=excerpt,
        )

        return revocation
