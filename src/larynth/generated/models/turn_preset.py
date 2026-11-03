from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.turn_preset_key import TurnPresetKey, check_turn_preset_key

if TYPE_CHECKING:
    from ..models.interruption_profile import InterruptionProfile
    from ..models.turn_profile import TurnProfile


T = TypeVar("T", bound="TurnPreset")


@_attrs_define
class TurnPreset:
    """
    Attributes:
        interruption_profile (InterruptionProfile):
        key (TurnPresetKey):
        position (int):
        recommended (bool):
        turn_profile (TurnProfile):
    """

    interruption_profile: InterruptionProfile
    key: TurnPresetKey
    position: int
    recommended: bool
    turn_profile: TurnProfile

    def to_dict(self) -> dict[str, Any]:
        interruption_profile = self.interruption_profile.to_dict()

        key: str = self.key

        position = self.position

        recommended = self.recommended

        turn_profile = self.turn_profile.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "interruption_profile": interruption_profile,
                "key": key,
                "position": position,
                "recommended": recommended,
                "turn_profile": turn_profile,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.interruption_profile import InterruptionProfile
        from ..models.turn_profile import TurnProfile

        d = dict(src_dict)
        interruption_profile = InterruptionProfile.from_dict(
            d.pop("interruption_profile")
        )

        key = check_turn_preset_key(d.pop("key"))

        position = d.pop("position")

        recommended = d.pop("recommended")

        turn_profile = TurnProfile.from_dict(d.pop("turn_profile"))

        turn_preset = cls(
            interruption_profile=interruption_profile,
            key=key,
            position=position,
            recommended=recommended,
            turn_profile=turn_profile,
        )

        return turn_preset
