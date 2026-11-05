from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="UsageLines")


@_attrs_define
class UsageLines:
    """
    Attributes:
        agent_micro (int):
        branded_micro (int):
        bridged_micro (int):
        byo_micro (int):
        forward_micro (int):
        number_micro (int):
        premium_micro (int):
        simulation_micro (int):
    """

    agent_micro: int
    branded_micro: int
    bridged_micro: int
    byo_micro: int
    forward_micro: int
    number_micro: int
    premium_micro: int
    simulation_micro: int

    def to_dict(self) -> dict[str, Any]:
        agent_micro = self.agent_micro

        branded_micro = self.branded_micro

        bridged_micro = self.bridged_micro

        byo_micro = self.byo_micro

        forward_micro = self.forward_micro

        number_micro = self.number_micro

        premium_micro = self.premium_micro

        simulation_micro = self.simulation_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_micro": agent_micro,
                "branded_micro": branded_micro,
                "bridged_micro": bridged_micro,
                "byo_micro": byo_micro,
                "forward_micro": forward_micro,
                "number_micro": number_micro,
                "premium_micro": premium_micro,
                "simulation_micro": simulation_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        agent_micro = d.pop("agent_micro")

        branded_micro = d.pop("branded_micro")

        bridged_micro = d.pop("bridged_micro")

        byo_micro = d.pop("byo_micro")

        forward_micro = d.pop("forward_micro")

        number_micro = d.pop("number_micro")

        premium_micro = d.pop("premium_micro")

        simulation_micro = d.pop("simulation_micro")

        usage_lines = cls(
            agent_micro=agent_micro,
            branded_micro=branded_micro,
            bridged_micro=bridged_micro,
            byo_micro=byo_micro,
            forward_micro=forward_micro,
            number_micro=number_micro,
            premium_micro=premium_micro,
            simulation_micro=simulation_micro,
        )

        return usage_lines
