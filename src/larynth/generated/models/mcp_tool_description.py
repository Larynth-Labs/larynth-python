from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="McpToolDescription")


@_attrs_define
class McpToolDescription:
    """
    Attributes:
        description (str):
    """

    description: str

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description")

        mcp_tool_description = cls(
            description=description,
        )

        return mcp_tool_description
