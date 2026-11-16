from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AlertMatch")


@_attrs_define
class AlertMatch:
    """
    Attributes:
        field (str):
        value (Any):
    """

    field: str
    value: Any

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        value = self.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "field": field,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        field = d.pop("field")

        value = d.pop("value")

        alert_match = cls(
            field=field,
            value=value,
        )

        return alert_match
