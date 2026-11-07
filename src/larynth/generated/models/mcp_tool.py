from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.mcp_tool_state import McpToolState, check_mcp_tool_state
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_tool_input_schema import McpToolInputSchema
    from ..models.mcp_tool_previous import McpToolPrevious


T = TypeVar("T", bound="McpTool")


@_attrs_define
class McpTool:
    """
    Attributes:
        description (str): Our description; the only text the call-time model sees besides the input schema
        enabled (bool):
        id (UUID):
        input_schema (McpToolInputSchema):
        sha256 (str): Hex hash of name, upstream description and input schema
        state (McpToolState):
        upstream_name (str):
        write (bool):
        approved_sha256 (str | Unset):
        previous (McpToolPrevious | Unset):
        upstream_description (str | Unset): The server's own text; returned to Owners and Admins only
    """

    description: str
    enabled: bool
    id: UUID
    input_schema: McpToolInputSchema
    sha256: str
    state: McpToolState
    upstream_name: str
    write: bool
    approved_sha256: str | Unset = UNSET
    previous: McpToolPrevious | Unset = UNSET
    upstream_description: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        enabled = self.enabled

        id = str(self.id)

        input_schema = self.input_schema.to_dict()

        sha256 = self.sha256

        state: str = self.state

        upstream_name = self.upstream_name

        write = self.write

        approved_sha256 = self.approved_sha256

        previous: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        upstream_description = self.upstream_description

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "enabled": enabled,
                "id": id,
                "input_schema": input_schema,
                "sha256": sha256,
                "state": state,
                "upstream_name": upstream_name,
                "write": write,
            }
        )
        if approved_sha256 is not UNSET:
            field_dict["approved_sha256"] = approved_sha256
        if previous is not UNSET:
            field_dict["previous"] = previous
        if upstream_description is not UNSET:
            field_dict["upstream_description"] = upstream_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_tool_input_schema import McpToolInputSchema
        from ..models.mcp_tool_previous import McpToolPrevious

        d = dict(src_dict)
        description = d.pop("description")

        enabled = d.pop("enabled")

        id = UUID(d.pop("id"))

        input_schema = McpToolInputSchema.from_dict(d.pop("input_schema"))

        sha256 = d.pop("sha256")

        state = check_mcp_tool_state(d.pop("state"))

        upstream_name = d.pop("upstream_name")

        write = d.pop("write")

        approved_sha256 = d.pop("approved_sha256", UNSET)

        _previous = d.pop("previous", UNSET)
        previous: McpToolPrevious | Unset
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = McpToolPrevious.from_dict(_previous)

        upstream_description = d.pop("upstream_description", UNSET)

        mcp_tool = cls(
            description=description,
            enabled=enabled,
            id=id,
            input_schema=input_schema,
            sha256=sha256,
            state=state,
            upstream_name=upstream_name,
            write=write,
            approved_sha256=approved_sha256,
            previous=previous,
            upstream_description=upstream_description,
        )

        return mcp_tool
