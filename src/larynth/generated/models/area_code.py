from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AreaCode")


@_attrs_define
class AreaCode:
    """
    Attributes:
        cities (list[str]):
        npa (str):
        timezones (list[str]):
        city (str | Unset): Largest city served
        overlay_of (str | Unset):
        state (str | Unset):
    """

    cities: list[str]
    npa: str
    timezones: list[str]
    city: str | Unset = UNSET
    overlay_of: str | Unset = UNSET
    state: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cities = self.cities

        npa = self.npa

        timezones = self.timezones

        city = self.city

        overlay_of = self.overlay_of

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "cities": cities,
                "npa": npa,
                "timezones": timezones,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if overlay_of is not UNSET:
            field_dict["overlay_of"] = overlay_of
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cities = cast(list[str], d.pop("cities"))

        npa = d.pop("npa")

        timezones = cast(list[str], d.pop("timezones"))

        city = d.pop("city", UNSET)

        overlay_of = d.pop("overlay_of", UNSET)

        state = d.pop("state", UNSET)

        area_code = cls(
            cities=cities,
            npa=npa,
            timezones=timezones,
            city=city,
            overlay_of=overlay_of,
            state=state,
        )

        return area_code
