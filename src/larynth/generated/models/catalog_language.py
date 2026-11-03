from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogLanguage")


@_attrs_define
class CatalogLanguage:
    """
    Attributes:
        code (str): Language code, for example en
        name (str):
    """

    code: str
    name: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        code = d.pop("code")

        name = d.pop("name")

        catalog_language = cls(
            code=code,
            name=name,
        )

        return catalog_language
