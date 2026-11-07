from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.assistant_tool_class import AssistantToolClass, check_assistant_tool_class
from ..models.assistant_tool_kind import AssistantToolKind, check_assistant_tool_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_tool_config import AssistantToolConfig
    from ..models.assistant_tool_json_schema import AssistantToolJsonSchema
    from ..models.calendar_tool_config import CalendarToolConfig
    from ..models.transfer_destination import TransferDestination


T = TypeVar("T", bound="AssistantTool")


@_attrs_define
class AssistantTool:
    """
    Attributes:
        class_ (AssistantToolClass):
        description (str):
        json_schema (AssistantToolJsonSchema):
        kind (AssistantToolKind):
        name (str):
        calendar_tool (CalendarToolConfig | Unset):
        config (AssistantToolConfig | Unset):
        destinations (list[TransferDestination] | Unset): Transfer tools only (kind transfer, name transfer_call): where
            the agent may transfer the caller
        endpoint_ref (str | Unset):
        mcp_tool_id (UUID | Unset): mcp: an approved MCP tool
        stale (bool | Unset): mcp: the tool changed on its server or lost its approval. The draft keeps the old pin;
            review and approve the tool, then save and publish again
        timeout_ms (int | Unset):  Default: 8000.
        workspace_tool_id (UUID | Unset): workspace_http: the HTTP tool from the library
        workspace_tool_revision (int | Unset): workspace_http: pinned revision; set by the server when the draft is
            saved
    """

    class_: AssistantToolClass
    description: str
    json_schema: AssistantToolJsonSchema
    kind: AssistantToolKind
    name: str
    calendar_tool: CalendarToolConfig | Unset = UNSET
    config: AssistantToolConfig | Unset = UNSET
    destinations: list[TransferDestination] | Unset = UNSET
    endpoint_ref: str | Unset = UNSET
    mcp_tool_id: UUID | Unset = UNSET
    stale: bool | Unset = UNSET
    timeout_ms: int | Unset = 8000
    workspace_tool_id: UUID | Unset = UNSET
    workspace_tool_revision: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        class_: str = self.class_

        description = self.description

        json_schema = self.json_schema.to_dict()

        kind: str = self.kind

        name = self.name

        calendar_tool: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar_tool, Unset):
            calendar_tool = self.calendar_tool.to_dict()

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        destinations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.destinations, Unset):
            destinations = []
            for destinations_item_data in self.destinations:
                destinations_item = destinations_item_data.to_dict()
                destinations.append(destinations_item)

        endpoint_ref = self.endpoint_ref

        mcp_tool_id: str | Unset = UNSET
        if not isinstance(self.mcp_tool_id, Unset):
            mcp_tool_id = str(self.mcp_tool_id)

        stale = self.stale

        timeout_ms = self.timeout_ms

        workspace_tool_id: str | Unset = UNSET
        if not isinstance(self.workspace_tool_id, Unset):
            workspace_tool_id = str(self.workspace_tool_id)

        workspace_tool_revision = self.workspace_tool_revision

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "class": class_,
                "description": description,
                "json_schema": json_schema,
                "kind": kind,
                "name": name,
            }
        )
        if calendar_tool is not UNSET:
            field_dict["calendar_tool"] = calendar_tool
        if config is not UNSET:
            field_dict["config"] = config
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if endpoint_ref is not UNSET:
            field_dict["endpoint_ref"] = endpoint_ref
        if mcp_tool_id is not UNSET:
            field_dict["mcp_tool_id"] = mcp_tool_id
        if stale is not UNSET:
            field_dict["stale"] = stale
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms
        if workspace_tool_id is not UNSET:
            field_dict["workspace_tool_id"] = workspace_tool_id
        if workspace_tool_revision is not UNSET:
            field_dict["workspace_tool_revision"] = workspace_tool_revision

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_tool_config import AssistantToolConfig
        from ..models.assistant_tool_json_schema import AssistantToolJsonSchema
        from ..models.calendar_tool_config import CalendarToolConfig
        from ..models.transfer_destination import TransferDestination

        d = dict(src_dict)
        class_ = check_assistant_tool_class(d.pop("class"))

        description = d.pop("description")

        json_schema = AssistantToolJsonSchema.from_dict(d.pop("json_schema"))

        kind = check_assistant_tool_kind(d.pop("kind"))

        name = d.pop("name")

        _calendar_tool = d.pop("calendar_tool", UNSET)
        calendar_tool: CalendarToolConfig | Unset
        if isinstance(_calendar_tool, Unset):
            calendar_tool = UNSET
        else:
            calendar_tool = CalendarToolConfig.from_dict(_calendar_tool)

        _config = d.pop("config", UNSET)
        config: AssistantToolConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = AssistantToolConfig.from_dict(_config)

        _destinations = d.pop("destinations", UNSET)
        destinations: list[TransferDestination] | Unset = UNSET
        if _destinations is not UNSET:
            destinations = []
            for destinations_item_data in _destinations:
                destinations_item = TransferDestination.from_dict(
                    destinations_item_data
                )

                destinations.append(destinations_item)

        endpoint_ref = d.pop("endpoint_ref", UNSET)

        _mcp_tool_id = d.pop("mcp_tool_id", UNSET)
        mcp_tool_id: UUID | Unset
        if isinstance(_mcp_tool_id, Unset):
            mcp_tool_id = UNSET
        else:
            mcp_tool_id = UUID(_mcp_tool_id)

        stale = d.pop("stale", UNSET)

        timeout_ms = d.pop("timeout_ms", UNSET)

        _workspace_tool_id = d.pop("workspace_tool_id", UNSET)
        workspace_tool_id: UUID | Unset
        if isinstance(_workspace_tool_id, Unset):
            workspace_tool_id = UNSET
        else:
            workspace_tool_id = UUID(_workspace_tool_id)

        workspace_tool_revision = d.pop("workspace_tool_revision", UNSET)

        assistant_tool = cls(
            class_=class_,
            description=description,
            json_schema=json_schema,
            kind=kind,
            name=name,
            calendar_tool=calendar_tool,
            config=config,
            destinations=destinations,
            endpoint_ref=endpoint_ref,
            mcp_tool_id=mcp_tool_id,
            stale=stale,
            timeout_ms=timeout_ms,
            workspace_tool_id=workspace_tool_id,
            workspace_tool_revision=workspace_tool_revision,
        )

        return assistant_tool
