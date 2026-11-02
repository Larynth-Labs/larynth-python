from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableNumber")


@_attrs_define
class AvailableNumber:
    """
    Attributes:
        country (str):
        e164 (str):
        monthly_price_micro (int): Rental price in micro-USD per month
        region (str | Unset):
    """

    country: str
    e164: str
    monthly_price_micro: int
    region: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        e164 = self.e164

        monthly_price_micro = self.monthly_price_micro

        region = self.region

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "e164": e164,
                "monthly_price_micro": monthly_price_micro,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country")

        e164 = d.pop("e164")

        monthly_price_micro = d.pop("monthly_price_micro")

        region = d.pop("region", UNSET)

        available_number = cls(
            country=country,
            e164=e164,
            monthly_price_micro=monthly_price_micro,
            region=region,
        )

        return available_number
