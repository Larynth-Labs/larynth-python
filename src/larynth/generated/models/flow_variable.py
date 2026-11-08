from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowVariable")


@_attrs_define
class FlowVariable:
    """
    Attributes:
        name (str):
        type_ (str):
        default (Any | Unset):
        description (str | Unset):
        enum (list[str] | Unset):
        input_ (bool | Unset):
        pii (bool | Unset):
        required_input (bool | Unset):
    """

    name: str
    type_: str
    default: Any | Unset = UNSET
    description: str | Unset = UNSET
    enum: list[str] | Unset = UNSET
    input_: bool | Unset = UNSET
    pii: bool | Unset = UNSET
    required_input: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        default = self.default

        description = self.description

        enum: list[str] | Unset = UNSET
        if not isinstance(self.enum, Unset):
            enum = self.enum

        input_ = self.input_

        pii = self.pii

        required_input = self.required_input

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if enum is not UNSET:
            field_dict["enum"] = enum
        if input_ is not UNSET:
            field_dict["input"] = input_
        if pii is not UNSET:
            field_dict["pii"] = pii
        if required_input is not UNSET:
            field_dict["required_input"] = required_input

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        default = d.pop("default", UNSET)

        description = d.pop("description", UNSET)

        enum = cast(list[str], d.pop("enum", UNSET))

        input_ = d.pop("input", UNSET)

        pii = d.pop("pii", UNSET)

        required_input = d.pop("required_input", UNSET)

        flow_variable = cls(
            name=name,
            type_=type_,
            default=default,
            description=description,
            enum=enum,
            input_=input_,
            pii=pii,
            required_input=required_input,
        )

        return flow_variable
