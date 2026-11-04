from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.routing_target_mode import RoutingTargetMode, check_routing_target_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="RoutingTarget")


@_attrs_define
class RoutingTarget:
    """
    Attributes:
        mode (RoutingTargetMode):
        assistant_id (UUID | Unset): Required for assistant; the agent must be live or paused
        forward_e164 (str | Unset): Required for forward; a US number that is not 911/933, premium or another
            workspace's Larynth number
    """

    mode: RoutingTargetMode
    assistant_id: UUID | Unset = UNSET
    forward_e164: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        assistant_id: str | Unset = UNSET
        if not isinstance(self.assistant_id, Unset):
            assistant_id = str(self.assistant_id)

        forward_e164 = self.forward_e164

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if assistant_id is not UNSET:
            field_dict["assistant_id"] = assistant_id
        if forward_e164 is not UNSET:
            field_dict["forward_e164"] = forward_e164

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = check_routing_target_mode(d.pop("mode"))

        _assistant_id = d.pop("assistant_id", UNSET)
        assistant_id: UUID | Unset
        if isinstance(_assistant_id, Unset):
            assistant_id = UNSET
        else:
            assistant_id = UUID(_assistant_id)

        forward_e164 = d.pop("forward_e164", UNSET)

        routing_target = cls(
            mode=mode,
            assistant_id=assistant_id,
            forward_e164=forward_e164,
        )

        return routing_target
