from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowLimits")


@_attrs_define
class FlowLimits:
    """
    Attributes:
        max_node_visits (int | Unset):
        max_transitions (int | Unset):
    """

    max_node_visits: int | Unset = UNSET
    max_transitions: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        max_node_visits = self.max_node_visits

        max_transitions = self.max_transitions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if max_node_visits is not UNSET:
            field_dict["max_node_visits"] = max_node_visits
        if max_transitions is not UNSET:
            field_dict["max_transitions"] = max_transitions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_node_visits = d.pop("max_node_visits", UNSET)

        max_transitions = d.pop("max_transitions", UNSET)

        flow_limits = cls(
            max_node_visits=max_node_visits,
            max_transitions=max_transitions,
        )

        return flow_limits
