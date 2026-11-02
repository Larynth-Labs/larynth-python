from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.assistant_tool_class import AssistantToolClass, check_assistant_tool_class
from ..models.assistant_tool_kind import AssistantToolKind, check_assistant_tool_kind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assistant_tool_config import AssistantToolConfig
    from ..models.assistant_tool_json_schema import AssistantToolJsonSchema
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
        config (AssistantToolConfig | Unset):
        destinations (list[TransferDestination] | Unset): Transfer tools only (kind transfer, name transfer_call): where
            the agent may transfer the caller
        endpoint_ref (str | Unset):
        timeout_ms (int | Unset):  Default: 8000.
    """

    class_: AssistantToolClass
    description: str
    json_schema: AssistantToolJsonSchema
    kind: AssistantToolKind
    name: str
    config: AssistantToolConfig | Unset = UNSET
    destinations: list[TransferDestination] | Unset = UNSET
    endpoint_ref: str | Unset = UNSET
    timeout_ms: int | Unset = 8000

    def to_dict(self) -> dict[str, Any]:
        class_: str = self.class_

        description = self.description

        json_schema = self.json_schema.to_dict()

        kind: str = self.kind

        name = self.name

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

        timeout_ms = self.timeout_ms

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
        if config is not UNSET:
            field_dict["config"] = config
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if endpoint_ref is not UNSET:
            field_dict["endpoint_ref"] = endpoint_ref
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assistant_tool_config import AssistantToolConfig
        from ..models.assistant_tool_json_schema import AssistantToolJsonSchema
        from ..models.transfer_destination import TransferDestination

        d = dict(src_dict)
        class_ = check_assistant_tool_class(d.pop("class"))

        description = d.pop("description")

        json_schema = AssistantToolJsonSchema.from_dict(d.pop("json_schema"))

        kind = check_assistant_tool_kind(d.pop("kind"))

        name = d.pop("name")

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

        timeout_ms = d.pop("timeout_ms", UNSET)

        assistant_tool = cls(
            class_=class_,
            description=description,
            json_schema=json_schema,
            kind=kind,
            name=name,
            config=config,
            destinations=destinations,
            endpoint_ref=endpoint_ref,
            timeout_ms=timeout_ms,
        )

        return assistant_tool
