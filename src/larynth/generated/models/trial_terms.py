from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.trial_terms_covers_item import (
    TrialTermsCoversItem,
    check_trial_terms_covers_item,
)

T = TypeVar("T", bound="TrialTerms")


@_attrs_define
class TrialTerms:
    """
    Attributes:
        covers (list[TrialTermsCoversItem]): Call kinds free credit pays for
        credit_micro (int): Free credit granted at signup; never refundable, never expires
    """

    covers: list[TrialTermsCoversItem]
    credit_micro: int

    def to_dict(self) -> dict[str, Any]:
        covers = []
        for covers_item_data in self.covers:
            covers_item: str = covers_item_data
            covers.append(covers_item)

        credit_micro = self.credit_micro

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "covers": covers,
                "credit_micro": credit_micro,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        covers = []
        _covers = d.pop("covers")
        for covers_item_data in _covers:
            covers_item = check_trial_terms_covers_item(covers_item_data)

            covers.append(covers_item)

        credit_micro = d.pop("credit_micro")

        trial_terms = cls(
            covers=covers,
            credit_micro=credit_micro,
        )

        return trial_terms
