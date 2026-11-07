from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RefreshDraftToolsRequest")


@_attrs_define
class RefreshDraftToolsRequest:
    """
    Attributes:
        tool_ids (list[str] | Unset): Workspace tool ids; unset refreshes all
    """

    tool_ids: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        tool_ids: list[str] | Unset = UNSET
        if not isinstance(self.tool_ids, Unset):
            tool_ids = self.tool_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if tool_ids is not UNSET:
            field_dict["tool_ids"] = tool_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tool_ids = cast(list[str], d.pop("tool_ids", UNSET))

        refresh_draft_tools_request = cls(
            tool_ids=tool_ids,
        )

        return refresh_draft_tools_request
