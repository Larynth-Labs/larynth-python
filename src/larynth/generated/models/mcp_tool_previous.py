from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.mcp_tool_previous_input_schema import McpToolPreviousInputSchema


T = TypeVar("T", bound="McpToolPrevious")


@_attrs_define
class McpToolPrevious:
    """
    Attributes:
        input_schema (McpToolPreviousInputSchema):
        upstream_description (str):
    """

    input_schema: McpToolPreviousInputSchema
    upstream_description: str

    def to_dict(self) -> dict[str, Any]:
        input_schema = self.input_schema.to_dict()

        upstream_description = self.upstream_description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "input_schema": input_schema,
                "upstream_description": upstream_description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_tool_previous_input_schema import McpToolPreviousInputSchema

        d = dict(src_dict)
        input_schema = McpToolPreviousInputSchema.from_dict(d.pop("input_schema"))

        upstream_description = d.pop("upstream_description")

        mcp_tool_previous = cls(
            input_schema=input_schema,
            upstream_description=upstream_description,
        )

        return mcp_tool_previous
