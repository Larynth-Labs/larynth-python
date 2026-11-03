from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishAssistantVersionRequest")


@_attrs_define
class PublishAssistantVersionRequest:
    """
    Attributes:
        note (str | Unset):
    """

    note: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        note = self.note

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        note = d.pop("note", UNSET)

        publish_assistant_version_request = cls(
            note=note,
        )

        return publish_assistant_version_request
