from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.contact_last_call_direction import (
    ContactLastCallDirection,
    check_contact_last_call_direction,
)

T = TypeVar("T", bound="ContactLastCall")


@_attrs_define
class ContactLastCall:
    """
    Attributes:
        at (datetime.datetime):
        call_id (str):
        direction (ContactLastCallDirection):
    """

    at: datetime.datetime
    call_id: str
    direction: ContactLastCallDirection

    def to_dict(self) -> dict[str, Any]:
        at = self.at.isoformat()

        call_id = self.call_id

        direction: str = self.direction

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "at": at,
                "call_id": call_id,
                "direction": direction,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        at = datetime.datetime.fromisoformat(d.pop("at"))

        call_id = d.pop("call_id")

        direction = check_contact_last_call_direction(d.pop("direction"))

        contact_last_call = cls(
            at=at,
            call_id=call_id,
            direction=direction,
        )

        return contact_last_call
