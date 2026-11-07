from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_assignment import FlowAssignment
    from ..models.flow_bridge import FlowBridge
    from ..models.flow_condition import FlowCondition


T = TypeVar("T", bound="FlowEdge")


@_attrs_define
class FlowEdge:
    """
    Attributes:
        id (str):
        to (str):
        when (FlowCondition):
        bridge (FlowBridge | Unset):
        set_ (list[FlowAssignment] | Unset):
    """

    id: str
    to: str
    when: FlowCondition
    bridge: FlowBridge | Unset = UNSET
    set_: list[FlowAssignment] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        to = self.to

        when = self.when.to_dict()

        bridge: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bridge, Unset):
            bridge = self.bridge.to_dict()

        set_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = []
            for set_item_data in self.set_:
                set_item = set_item_data.to_dict()
                set_.append(set_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "to": to,
                "when": when,
            }
        )
        if bridge is not UNSET:
            field_dict["bridge"] = bridge
        if set_ is not UNSET:
            field_dict["set"] = set_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_assignment import FlowAssignment
        from ..models.flow_bridge import FlowBridge
        from ..models.flow_condition import FlowCondition

        d = dict(src_dict)
        id = d.pop("id")

        to = d.pop("to")

        when = FlowCondition.from_dict(d.pop("when"))

        _bridge = d.pop("bridge", UNSET)
        bridge: FlowBridge | Unset
        if isinstance(_bridge, Unset):
            bridge = UNSET
        else:
            bridge = FlowBridge.from_dict(_bridge)

        _set_ = d.pop("set", UNSET)
        set_: list[FlowAssignment] | Unset = UNSET
        if _set_ is not UNSET:
            set_ = []
            for set_item_data in _set_:
                set_item = FlowAssignment.from_dict(set_item_data)

                set_.append(set_item)

        flow_edge = cls(
            id=id,
            to=to,
            when=when,
            bridge=bridge,
            set_=set_,
        )

        return flow_edge
