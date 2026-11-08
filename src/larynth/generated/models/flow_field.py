from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowField")


@_attrs_define
class FlowField:
    """
    Attributes:
        variable (str):
        confirm (bool | Unset):
        pattern (str | Unset):
        required (bool | Unset):
    """

    variable: str
    confirm: bool | Unset = UNSET
    pattern: str | Unset = UNSET
    required: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        variable = self.variable

        confirm = self.confirm

        pattern = self.pattern

        required = self.required

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "variable": variable,
            }
        )
        if confirm is not UNSET:
            field_dict["confirm"] = confirm
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        variable = d.pop("variable")

        confirm = d.pop("confirm", UNSET)

        pattern = d.pop("pattern", UNSET)

        required = d.pop("required", UNSET)

        flow_field = cls(
            variable=variable,
            confirm=confirm,
            pattern=pattern,
            required=required,
        )

        return flow_field
