from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddSpamAllowRequest")


@_attrs_define
class AddSpamAllowRequest:
    """
    Attributes:
        e164 (str):
        note (str | Unset):
    """

    e164: str
    note: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        e164 = self.e164

        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "e164": e164,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        e164 = d.pop("e164")

        note = d.pop("note", UNSET)

        add_spam_allow_request = cls(
            e164=e164,
            note=note,
        )

        return add_spam_allow_request
