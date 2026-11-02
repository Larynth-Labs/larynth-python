from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDNCRequest")


@_attrs_define
class CreateDNCRequest:
    """
    Attributes:
        e164 (str):
        category (str | Unset): Opt-out scope: telemarketing covers all marketing calls, another value one informational
            category; empty covers every call
        reason (str | Unset):
    """

    e164: str
    category: str | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        category = self.category

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        category = d.pop("category", UNSET)

        reason = d.pop("reason", UNSET)

        create_dnc_request = cls(
            e164=e164,
            category=category,
            reason=reason,
        )

        return create_dnc_request
