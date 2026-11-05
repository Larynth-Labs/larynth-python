from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.free_rule import FreeRule
    from ..models.launch_price import LaunchPrice
    from ..models.rate_card_group import RateCardGroup
    from ..models.trial_terms import TrialTerms


T = TypeVar("T", bound="RateCard")


@_attrs_define
class RateCard:
    """
    Attributes:
        bundles_note_key (str):
        free_rules (list[FreeRule]):
        groups (list[RateCardGroup]):
        trial (TrialTerms):
        launch_price (LaunchPrice | Unset):
    """

    bundles_note_key: str
    free_rules: list[FreeRule]
    groups: list[RateCardGroup]
    trial: TrialTerms
    launch_price: LaunchPrice | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        bundles_note_key = self.bundles_note_key

        free_rules = []
        for free_rules_item_data in self.free_rules:
            free_rules_item = free_rules_item_data.to_dict()
            free_rules.append(free_rules_item)

        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)

        trial = self.trial.to_dict()

        launch_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.launch_price, Unset):
            launch_price = self.launch_price.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "bundles_note_key": bundles_note_key,
                "free_rules": free_rules,
                "groups": groups,
                "trial": trial,
            }
        )
        if launch_price is not UNSET:
            field_dict["launch_price"] = launch_price

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.free_rule import FreeRule
        from ..models.launch_price import LaunchPrice
        from ..models.rate_card_group import RateCardGroup
        from ..models.trial_terms import TrialTerms

        d = dict(src_dict)
        bundles_note_key = d.pop("bundles_note_key")

        free_rules = []
        _free_rules = d.pop("free_rules")
        for free_rules_item_data in _free_rules:
            free_rules_item = FreeRule.from_dict(free_rules_item_data)

            free_rules.append(free_rules_item)

        groups = []
        _groups = d.pop("groups")
        for groups_item_data in _groups:
            groups_item = RateCardGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        trial = TrialTerms.from_dict(d.pop("trial"))

        _launch_price = d.pop("launch_price", UNSET)
        launch_price: LaunchPrice | Unset
        if isinstance(_launch_price, Unset):
            launch_price = UNSET
        else:
            launch_price = LaunchPrice.from_dict(_launch_price)

        rate_card = cls(
            bundles_note_key=bundles_note_key,
            free_rules=free_rules,
            groups=groups,
            trial=trial,
            launch_price=launch_price,
        )

        return rate_card
