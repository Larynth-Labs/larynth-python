from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.left_out_contact_reason import (
    LeftOutContactReason,
    check_left_out_contact_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LeftOutContact")


@_attrs_define
class LeftOutContact:
    """
    Attributes:
        contact_id (UUID):
        reason (LeftOutContactReason):
        name (str | Unset):
    """

    contact_id: UUID
    reason: LeftOutContactReason
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        contact_id = str(self.contact_id)

        reason: str = self.reason

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "contact_id": contact_id,
                "reason": reason,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        contact_id = UUID(d.pop("contact_id"))

        reason = check_left_out_contact_reason(d.pop("reason"))

        name = d.pop("name", UNSET)

        left_out_contact = cls(
            contact_id=contact_id,
            reason=reason,
            name=name,
        )

        return left_out_contact
