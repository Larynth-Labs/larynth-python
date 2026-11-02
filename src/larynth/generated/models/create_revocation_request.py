from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRevocationRequest")


@_attrs_define
class CreateRevocationRequest:
    """
    Attributes:
        e164 (str):
        category (str | Unset): Opt-out scope: telemarketing covers all marketing calls, another value one informational
            category; empty covers every call
        excerpt (str | Unset):
        revoked_at (datetime.datetime | Unset): Defaults to now
    """

    e164: str
    category: str | Unset = UNSET
    excerpt: str | Unset = UNSET
    revoked_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        category = self.category

        excerpt = self.excerpt

        revoked_at: str | Unset = UNSET
        if not isinstance(self.revoked_at, Unset):
            revoked_at = self.revoked_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if excerpt is not UNSET:
            field_dict["excerpt"] = excerpt
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        category = d.pop("category", UNSET)

        excerpt = d.pop("excerpt", UNSET)

        _revoked_at = d.pop("revoked_at", UNSET)
        revoked_at: datetime.datetime | Unset
        if isinstance(_revoked_at, Unset):
            revoked_at = UNSET
        else:
            revoked_at = datetime.datetime.fromisoformat(_revoked_at)

        create_revocation_request = cls(
            e164=e164,
            category=category,
            excerpt=excerpt,
            revoked_at=revoked_at,
        )

        return create_revocation_request
