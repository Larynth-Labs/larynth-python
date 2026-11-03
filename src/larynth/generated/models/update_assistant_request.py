from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssistantRequest")


@_attrs_define
class UpdateAssistantRequest:
    """
    Attributes:
        description (str | Unset):
        latency_target_ms (int | Unset):
        name (str | Unset):
    """

    description: str | Unset = UNSET
    latency_target_ms: int | Unset = UNSET
    name: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        latency_target_ms = self.latency_target_ms

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if latency_target_ms is not UNSET:
            field_dict["latency_target_ms"] = latency_target_ms
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        latency_target_ms = d.pop("latency_target_ms", UNSET)

        name = d.pop("name", UNSET)

        update_assistant_request = cls(
            description=description,
            latency_target_ms=latency_target_ms,
            name=name,
        )

        return update_assistant_request
