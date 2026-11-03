from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBlockedCallerRequest")


@_attrs_define
class CreateBlockedCallerRequest:
    """
    Attributes:
        call_id (str | Unset): Block the caller of this call
        e164 (str | Unset): Set e164 or call_id
        reason (str | Unset):
    """

    call_id: str | Unset = UNSET
    e164: str | Unset = UNSET
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        call_id = self.call_id

        e164 = self.e164

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if call_id is not UNSET:
            field_dict["call_id"] = call_id
        if e164 is not UNSET:
            field_dict["e164"] = e164
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_id = d.pop("call_id", UNSET)

        e164 = d.pop("e164", UNSET)

        reason = d.pop("reason", UNSET)

        create_blocked_caller_request = cls(
            call_id=call_id,
            e164=e164,
            reason=reason,
        )

        return create_blocked_caller_request
