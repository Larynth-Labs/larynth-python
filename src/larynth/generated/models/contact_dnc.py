from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="ContactDNC")


@_attrs_define
class ContactDNC:
    """
    Attributes:
        listed (bool):
        sources (list[str]): tenant, opt_out, platform, national; national only from this workspace's own registry data
    """

    listed: bool
    sources: list[str]

    def to_dict(self) -> dict[str, Any]:
        listed = self.listed

        sources = self.sources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "listed": listed,
                "sources": sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        listed = d.pop("listed")

        sources = cast(list[str], d.pop("sources"))

        contact_dnc = cls(
            listed=listed,
            sources=sources,
        )

        return contact_dnc
