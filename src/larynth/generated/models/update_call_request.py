from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateCallRequest")


@_attrs_define
class UpdateCallRequest:
    """
    Attributes:
        flagged (bool | Unset):
        tags (list[str] | Unset): Each 1 to 24 characters, lower case; replaces the call's tags
    """

    flagged: bool | Unset = UNSET
    tags: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        flagged = self.flagged

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if flagged is not UNSET:
            field_dict["flagged"] = flagged
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        flagged = d.pop("flagged", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        update_call_request = cls(
            flagged=flagged,
            tags=tags,
        )

        return update_call_request
