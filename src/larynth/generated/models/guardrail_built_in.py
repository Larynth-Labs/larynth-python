from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..models.guardrail_built_in_category import (
    GuardrailBuiltInCategory,
    check_guardrail_built_in_category,
)

T = TypeVar("T", bound="GuardrailBuiltIn")


@_attrs_define
class GuardrailBuiltIn:
    """
    Attributes:
        category (GuardrailBuiltInCategory):
        description (str):
        key (str):
        title (str):
        version (int):
    """

    category: GuardrailBuiltInCategory
    description: str
    key: str
    title: str
    version: int

    def to_dict(self) -> dict[str, Any]:
        category: str = self.category

        description = self.description

        key = self.key

        title = self.title

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category": category,
                "description": description,
                "key": key,
                "title": title,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = check_guardrail_built_in_category(d.pop("category"))

        description = d.pop("description")

        key = d.pop("key")

        title = d.pop("title")

        version = d.pop("version")

        guardrail_built_in = cls(
            category=category,
            description=description,
            key=key,
            title=title,
            version=version,
        )

        return guardrail_built_in
