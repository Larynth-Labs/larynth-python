from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="KnowledgeResync")


@_attrs_define
class KnowledgeResync:
    """
    Attributes:
        enabled (bool):
        interval_days (int | Unset):  Default: 7.
    """

    enabled: bool
    interval_days: int | Unset = 7

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        interval_days = self.interval_days

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if interval_days is not UNSET:
            field_dict["interval_days"] = interval_days

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        interval_days = d.pop("interval_days", UNSET)

        knowledge_resync = cls(
            enabled=enabled,
            interval_days=interval_days,
        )

        return knowledge_resync
