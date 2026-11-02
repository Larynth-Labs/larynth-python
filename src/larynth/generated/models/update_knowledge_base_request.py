from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateKnowledgeBaseRequest")


@_attrs_define
class UpdateKnowledgeBaseRequest:
    """
    Attributes:
        description (str | Unset):
        name (str | Unset):
    """

    description: str | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        update_knowledge_base_request = cls(
            description=description,
            name=name,
        )

        return update_knowledge_base_request
