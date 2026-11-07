from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_limits import FlowLimits
    from ..models.flow_node import FlowNode
    from ..models.flow_subflow import FlowSubflow
    from ..models.flow_variable import FlowVariable


T = TypeVar("T", bound="FlowSpec")


@_attrs_define
class FlowSpec:
    """
    Attributes:
        entry_node_id (str):
        nodes (list[FlowNode]):
        schema (str):
        default_tools (list[str] | Unset):
        fallback_node_id (str | Unset):
        global_prompt_mode (str | Unset):
        limits (FlowLimits | Unset):
        subflows (list[FlowSubflow] | Unset):
        ui (Any | Unset):
        variables (list[FlowVariable] | Unset):
    """

    entry_node_id: str
    nodes: list[FlowNode]
    schema: str
    default_tools: list[str] | Unset = UNSET
    fallback_node_id: str | Unset = UNSET
    global_prompt_mode: str | Unset = UNSET
    limits: FlowLimits | Unset = UNSET
    subflows: list[FlowSubflow] | Unset = UNSET
    ui: Any | Unset = UNSET
    variables: list[FlowVariable] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        entry_node_id = self.entry_node_id

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        schema = self.schema

        default_tools: list[str] | Unset = UNSET
        if not isinstance(self.default_tools, Unset):
            default_tools = self.default_tools

        fallback_node_id = self.fallback_node_id

        global_prompt_mode = self.global_prompt_mode

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        subflows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subflows, Unset):
            subflows = []
            for subflows_item_data in self.subflows:
                subflows_item = subflows_item_data.to_dict()
                subflows.append(subflows_item)

        ui = self.ui

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entry_node_id": entry_node_id,
                "nodes": nodes,
                "schema": schema,
            }
        )
        if default_tools is not UNSET:
            field_dict["default_tools"] = default_tools
        if fallback_node_id is not UNSET:
            field_dict["fallback_node_id"] = fallback_node_id
        if global_prompt_mode is not UNSET:
            field_dict["global_prompt_mode"] = global_prompt_mode
        if limits is not UNSET:
            field_dict["limits"] = limits
        if subflows is not UNSET:
            field_dict["subflows"] = subflows
        if ui is not UNSET:
            field_dict["ui"] = ui
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_limits import FlowLimits
        from ..models.flow_node import FlowNode
        from ..models.flow_subflow import FlowSubflow
        from ..models.flow_variable import FlowVariable

        d = dict(src_dict)
        entry_node_id = d.pop("entry_node_id")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = FlowNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        schema = d.pop("schema")

        default_tools = cast(list[str], d.pop("default_tools", UNSET))

        fallback_node_id = d.pop("fallback_node_id", UNSET)

        global_prompt_mode = d.pop("global_prompt_mode", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: FlowLimits | Unset
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = FlowLimits.from_dict(_limits)

        _subflows = d.pop("subflows", UNSET)
        subflows: list[FlowSubflow] | Unset = UNSET
        if _subflows is not UNSET:
            subflows = []
            for subflows_item_data in _subflows:
                subflows_item = FlowSubflow.from_dict(subflows_item_data)

                subflows.append(subflows_item)

        ui = d.pop("ui", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: list[FlowVariable] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = FlowVariable.from_dict(variables_item_data)

                variables.append(variables_item)

        flow_spec = cls(
            entry_node_id=entry_node_id,
            nodes=nodes,
            schema=schema,
            default_tools=default_tools,
            fallback_node_id=fallback_node_id,
            global_prompt_mode=global_prompt_mode,
            limits=limits,
            subflows=subflows,
            ui=ui,
            variables=variables,
        )

        return flow_spec
