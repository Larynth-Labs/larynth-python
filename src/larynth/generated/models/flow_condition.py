from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_rule import FlowRule


T = TypeVar("T", bound="FlowCondition")


@_attrs_define
class FlowCondition:
    """
    Attributes:
        type_ (str):
        description (str | Unset):
        event (str | Unset):
        guard (FlowRule | Unset):
        rule (FlowRule | Unset):
    """

    type_: str
    description: str | Unset = UNSET
    event: str | Unset = UNSET
    guard: FlowRule | Unset = UNSET
    rule: FlowRule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        description = self.description

        event = self.event

        guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guard, Unset):
            guard = self.guard.to_dict()

        rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if event is not UNSET:
            field_dict["event"] = event
        if guard is not UNSET:
            field_dict["guard"] = guard
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_rule import FlowRule

        d = dict(src_dict)
        type_ = d.pop("type")

        description = d.pop("description", UNSET)

        event = d.pop("event", UNSET)

        _guard = d.pop("guard", UNSET)
        guard: FlowRule | Unset
        if isinstance(_guard, Unset):
            guard = UNSET
        else:
            guard = FlowRule.from_dict(_guard)

        _rule = d.pop("rule", UNSET)
        rule: FlowRule | Unset
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FlowRule.from_dict(_rule)

        flow_condition = cls(
            type_=type_,
            description=description,
            event=event,
            guard=guard,
            rule=rule,
        )

        return flow_condition
