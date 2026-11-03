from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.available_number_kind import (
    AvailableNumberKind,
    check_available_number_kind,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableNumber")


@_attrs_define
class AvailableNumber:
    """
    Attributes:
        country (str):
        e164 (str):
        monthly_price_micro (int): Rental price in micro-USD per month
        area_code (str | Unset):
        city (str | Unset):
        kind (AvailableNumberKind | Unset):
        region (str | Unset):
        state (str | Unset):
    """

    country: str
    e164: str
    monthly_price_micro: int
    area_code: str | Unset = UNSET
    city: str | Unset = UNSET
    kind: AvailableNumberKind | Unset = UNSET
    region: str | Unset = UNSET
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        e164 = self.e164

        monthly_price_micro = self.monthly_price_micro

        area_code = self.area_code

        city = self.city

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        region = self.region

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "country": country,
                "e164": e164,
                "monthly_price_micro": monthly_price_micro,
            }
        )
        if area_code is not UNSET:
            field_dict["area_code"] = area_code
        if city is not UNSET:
            field_dict["city"] = city
        if kind is not UNSET:
            field_dict["kind"] = kind
        if region is not UNSET:
            field_dict["region"] = region
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country")

        e164 = d.pop("e164")

        monthly_price_micro = d.pop("monthly_price_micro")

        area_code = d.pop("area_code", UNSET)

        city = d.pop("city", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: AvailableNumberKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_available_number_kind(_kind)

        region = d.pop("region", UNSET)

        state = d.pop("state", UNSET)

        available_number = cls(
            country=country,
            e164=e164,
            monthly_price_micro=monthly_price_micro,
            area_code=area_code,
            city=city,
            kind=kind,
            region=region,
            state=state,
        )

        return available_number
