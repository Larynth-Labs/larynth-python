from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.rate_card_line_rounding import (
    RateCardLineRounding,
    check_rate_card_line_rounding,
)
from ..models.rate_card_line_unit import RateCardLineUnit, check_rate_card_line_unit
from ..types import UNSET, Unset

T = TypeVar("T", bound="RateCardLine")


@_attrs_define
class RateCardLine:
    """
    Attributes:
        key (str):
        label_key (str):
        rounding (RateCardLineRounding):
        unit (RateCardLineUnit):
        list_price_micro (int | Unset): Price before the launch price
        model_label (str | Unset): Premium lines only, from the catalog row
        note_key (str | Unset):
        price_micro (int | Unset):
        provider_label (str | Unset): Premium lines only, from the catalog row
    """

    key: str
    label_key: str
    rounding: RateCardLineRounding
    unit: RateCardLineUnit
    list_price_micro: int | Unset = UNSET
    model_label: str | Unset = UNSET
    note_key: str | Unset = UNSET
    price_micro: int | Unset = UNSET
    provider_label: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        label_key = self.label_key

        rounding: str = self.rounding

        unit: str = self.unit

        list_price_micro = self.list_price_micro

        model_label = self.model_label

        note_key = self.note_key

        price_micro = self.price_micro

        provider_label = self.provider_label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "label_key": label_key,
                "rounding": rounding,
                "unit": unit,
            }
        )
        if list_price_micro is not UNSET:
            field_dict["list_price_micro"] = list_price_micro
        if model_label is not UNSET:
            field_dict["model_label"] = model_label
        if note_key is not UNSET:
            field_dict["note_key"] = note_key
        if price_micro is not UNSET:
            field_dict["price_micro"] = price_micro
        if provider_label is not UNSET:
            field_dict["provider_label"] = provider_label

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        label_key = d.pop("label_key")

        rounding = check_rate_card_line_rounding(d.pop("rounding"))

        unit = check_rate_card_line_unit(d.pop("unit"))

        list_price_micro = d.pop("list_price_micro", UNSET)

        model_label = d.pop("model_label", UNSET)

        note_key = d.pop("note_key", UNSET)

        price_micro = d.pop("price_micro", UNSET)

        provider_label = d.pop("provider_label", UNSET)

        rate_card_line = cls(
            key=key,
            label_key=label_key,
            rounding=rounding,
            unit=unit,
            list_price_micro=list_price_micro,
            model_label=model_label,
            note_key=note_key,
            price_micro=price_micro,
            provider_label=provider_label,
        )

        return rate_card_line
