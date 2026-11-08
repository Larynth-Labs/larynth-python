from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.mcp_server_status import McpServerStatus, check_mcp_server_status
from ..models.mcp_server_transport import McpServerTransport, check_mcp_server_transport
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_auth import McpAuth
    from ..models.mcp_tool import McpTool
    from ..models.tool_invocation_summary import ToolInvocationSummary
    from ..models.tool_use import ToolUse


T = TypeVar("T", bound="McpServer")


@_attrs_define
class McpServer:
    """
    Attributes:
        auth (McpAuth):
        created_at (datetime.datetime):
        id (UUID):
        name (str):
        status (McpServerStatus):
        tools (list[McpTool]):
        transport (McpServerTransport):
        updated_at (datetime.datetime):
        url (str):
        used_by (list[ToolUse]):
        error (str | Unset):
        last_discovered_at (datetime.datetime | Unset):
        last_invocation (ToolInvocationSummary | Unset):
    """

    auth: McpAuth
    created_at: datetime.datetime
    id: UUID
    name: str
    status: McpServerStatus
    tools: list[McpTool]
    transport: McpServerTransport
    updated_at: datetime.datetime
    url: str
    used_by: list[ToolUse]
    error: str | Unset = UNSET
    last_discovered_at: datetime.datetime | Unset = UNSET
    last_invocation: ToolInvocationSummary | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        auth = self.auth.to_dict()

        created_at = self.created_at.isoformat()

        id = str(self.id)

        name = self.name

        status: str = self.status

        tools = []
        for tools_item_data in self.tools:
            tools_item = tools_item_data.to_dict()
            tools.append(tools_item)

        transport: str = self.transport

        updated_at = self.updated_at.isoformat()

        url = self.url

        used_by = []
        for used_by_item_data in self.used_by:
            used_by_item = used_by_item_data.to_dict()
            used_by.append(used_by_item)

        error = self.error

        last_discovered_at: str | Unset = UNSET
        if not isinstance(self.last_discovered_at, Unset):
            last_discovered_at = self.last_discovered_at.isoformat()

        last_invocation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_invocation, Unset):
            last_invocation = self.last_invocation.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "auth": auth,
                "created_at": created_at,
                "id": id,
                "name": name,
                "status": status,
                "tools": tools,
                "transport": transport,
                "updated_at": updated_at,
                "url": url,
                "used_by": used_by,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if last_discovered_at is not UNSET:
            field_dict["last_discovered_at"] = last_discovered_at
        if last_invocation is not UNSET:
            field_dict["last_invocation"] = last_invocation

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mcp_auth import McpAuth
        from ..models.mcp_tool import McpTool
        from ..models.tool_invocation_summary import ToolInvocationSummary
        from ..models.tool_use import ToolUse

        d = dict(src_dict)
        auth = McpAuth.from_dict(d.pop("auth"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        id = UUID(d.pop("id"))

        name = d.pop("name")

        status = check_mcp_server_status(d.pop("status"))

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:
            tools_item = McpTool.from_dict(tools_item_data)

            tools.append(tools_item)

        transport = check_mcp_server_transport(d.pop("transport"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        url = d.pop("url")

        used_by = []
        _used_by = d.pop("used_by")
        for used_by_item_data in _used_by:
            used_by_item = ToolUse.from_dict(used_by_item_data)

            used_by.append(used_by_item)

        error = d.pop("error", UNSET)

        _last_discovered_at = d.pop("last_discovered_at", UNSET)
        last_discovered_at: datetime.datetime | Unset
        if isinstance(_last_discovered_at, Unset):
            last_discovered_at = UNSET
        else:
            last_discovered_at = datetime.datetime.fromisoformat(_last_discovered_at)

        _last_invocation = d.pop("last_invocation", UNSET)
        last_invocation: ToolInvocationSummary | Unset
        if isinstance(_last_invocation, Unset):
            last_invocation = UNSET
        else:
            last_invocation = ToolInvocationSummary.from_dict(_last_invocation)

        mcp_server = cls(
            auth=auth,
            created_at=created_at,
            id=id,
            name=name,
            status=status,
            tools=tools,
            transport=transport,
            updated_at=updated_at,
            url=url,
            used_by=used_by,
            error=error,
            last_discovered_at=last_discovered_at,
            last_invocation=last_invocation,
        )

        return mcp_server
