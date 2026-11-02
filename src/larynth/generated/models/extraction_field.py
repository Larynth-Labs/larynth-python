from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..models.extraction_field_type import (
    ExtractionFieldType,
    check_extraction_field_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractionField")


@_attrs_define
class ExtractionField:
    """
    Attributes:
        name (str):
        type_ (ExtractionFieldType):
        description (str | Unset):
        enum (list[str] | Unset): Allowed values; required for type enum, rejected otherwise
        required (bool | Unset): The model must return a non-null value
    """

    name: str
    type_: ExtractionFieldType
    description: str | Unset = UNSET
    enum: list[str] | Unset = UNSET
    required: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_: str = self.type_

        description = self.description

        enum: list[str] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        required = self.required

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if enum is not UNSET:
            field_dict["enum"] = enum
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = check_extraction_field_type(d.pop("type"))

        description = d.pop("description", UNSET)

        enum = cast(list[str], d.pop("enum", UNSET))

        required = d.pop("required", UNSET)

        extraction_field = cls(
            name=name,
            type_=type_,
            description=description,
            enum=enum,
            required=required,
        )

        return extraction_field
