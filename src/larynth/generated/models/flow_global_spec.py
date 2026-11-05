from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_rule import FlowRule


T = TypeVar("T", bound="FlowGlobalSpec")


@_attrs_define
class FlowGlobalSpec:
    """
    Attributes:
        cooldown_steps (int | Unset):
        description (str | Unset):
        exclude_nodes (list[str] | Unset):
        resume (str | Unset):
        rule (FlowRule | Unset):
    """

    cooldown_steps: int | Unset = UNSET
    description: str | Unset = UNSET
    exclude_nodes: list[str] | Unset = UNSET
    resume: str | Unset = UNSET
    rule: FlowRule | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cooldown_steps = self.cooldown_steps

        description = self.description

        exclude_nodes: list[str] | Unset = UNSET
        if not isinstance(self.exclude_nodes, Unset):
            exclude_nodes = self.exclude_nodes

        resume = self.resume

        rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cooldown_steps is not UNSET:
            field_dict["cooldown_steps"] = cooldown_steps
        if description is not UNSET:
            field_dict["description"] = description
        if exclude_nodes is not UNSET:
            field_dict["exclude_nodes"] = exclude_nodes
        if resume is not UNSET:
            field_dict["resume"] = resume
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.flow_rule import FlowRule

        d = dict(src_dict)
        cooldown_steps = d.pop("cooldown_steps", UNSET)

        description = d.pop("description", UNSET)

        exclude_nodes = cast(list[str], d.pop("exclude_nodes", UNSET))

        resume = d.pop("resume", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: FlowRule | Unset
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = FlowRule.from_dict(_rule)

        flow_global_spec = cls(
            cooldown_steps=cooldown_steps,
            description=description,
            exclude_nodes=exclude_nodes,
            resume=resume,
            rule=rule,
        )

        return flow_global_spec
