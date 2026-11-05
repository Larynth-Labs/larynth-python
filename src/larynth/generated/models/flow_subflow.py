from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.flow_node import FlowNode


T = TypeVar("T", bound="FlowSubflow")


@_attrs_define
class FlowSubflow:
    """
    Attributes:
        entry_node_id (str):
        id (str):
        name (str):
        nodes (list[FlowNode]):
    """

    entry_node_id: str
    id: str
    name: str
    nodes: list[FlowNode]

    def to_dict(self) -> dict[str, Any]:
        entry_node_id = self.entry_node_id

        id = self.id

        name = self.name

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entry_node_id": entry_node_id,
                "id": id,
                "name": name,
                "nodes": nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_node import FlowNode

        d = dict(src_dict)
        entry_node_id = d.pop("entry_node_id")

        id = d.pop("id")

        name = d.pop("name")

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = FlowNode.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        flow_subflow = cls(
            entry_node_id=entry_node_id,
            id=id,
            name=name,
            nodes=nodes,
        )

        return flow_subflow
