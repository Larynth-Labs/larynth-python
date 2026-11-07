from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ToolResponseHandling")


@_attrs_define
class ToolResponseHandling:
    """
    Attributes:
        max_bytes (int | Unset):  Default: 16384.
        pick (list[str] | Unset): JSON pointers into the response passed to the model; unset passes the trimmed body
        template (str | Unset):
    """

    max_bytes: int | Unset = 16384
    pick: list[str] | Unset = UNSET
    template: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_bytes = self.max_bytes

        pick: list[str] | Unset = UNSET
        if not isinstance(self.pick, Unset):
            pick = self.pick

        template = self.template

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_bytes is not UNSET:
            field_dict["max_bytes"] = max_bytes
        if pick is not UNSET:
            field_dict["pick"] = pick
        if template is not UNSET:
            field_dict["template"] = template

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_bytes = d.pop("max_bytes", UNSET)

        pick = cast(list[str], d.pop("pick", UNSET))

        template = d.pop("template", UNSET)

        tool_response_handling = cls(
            max_bytes=max_bytes,
            pick=pick,
            template=template,
        )

        return tool_response_handling
